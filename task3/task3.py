import sys
import json

def update_test_values(test_item, results_map):
    test_id = test_item.get("id")
    if test_id:
        test_item["value"] = results_map.get(test_id, None)

    sub_tests = test_item.get("values")
    if sub_tests:
        for sub_test in sub_tests:
            update_test_values(sub_test, results_map)

def test_results(results_file, tests_file, output_file):
    with open(results_file, 'r') as file:
        results_data = json.load(file)
        results_map = {entry['id']: entry['value'] for entry in results_data['values']}

    with open(tests_file, 'r') as file:
        tests_data = json.load(file)

    for test in tests_data["tests"]:
        update_test_values(test, results_map)

    with open(output_file, 'w') as file:
        json.dump(tests_data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("python task3.py <values_file> <tests_file> <output_file>")
    else:
        test_results(sys.argv[1], sys.argv[2], sys.argv[3])
