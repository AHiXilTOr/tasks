import sys

def circle_and_dot(circle_file, dot_file):
    with open(circle_file, 'r') as file:
        center_x, center_y = map(float, file.readline().split())
        radius = float(file.readline())

    with open(dot_file, 'r') as file:
        points = [tuple(map(float, line.split())) for line in file]

    def point_position(point, circle_center, radius):
        dx, dy = point[0] - circle_center[0], point[1] - circle_center[1]
        distance_squared = dx**2 + dy**2
        radius_squared = radius**2

        if distance_squared < radius_squared:
            return 1
        elif distance_squared > radius_squared:
            return 2
        return 0

    return [point_position(point, (center_x, center_y), radius) for point in points]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python task2.py <circle_file> <dot_file>")
    else:
        result = circle_and_dot(sys.argv[1], sys.argv[2])
        print(*result, sep="\n", end="\n")
