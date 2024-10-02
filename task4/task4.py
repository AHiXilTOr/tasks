import sys

def min_moves_to_equal_elements(file_path):
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file]
    
    nums.sort()
    n = len(nums)

    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = nums[n // 2 - 1]

    moves = sum(abs(num - median) for num in nums)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python task4.py <numbers_path>")
    else:
        result = min_moves_to_equal_elements(sys.argv[1])
        print(result)
