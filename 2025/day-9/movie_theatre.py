# https://adventofcode.com/2025/day/9

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    
    coordinates = []

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            grid_location = line.split(",")
            coordinates.append((int(grid_location[0]), int(grid_location[1])))

    return coordinates


def solve_part_one():
    red_x_coordinates = parse_input(INPUT_FILE)
    from pprint import pp
    # pp(red_x_coordinates)
    # pp(red_x_coordinates[0][0])
    largest_area = 0
    
    for i in range(0, len(red_x_coordinates)):
        for n in range(i+1, len(red_x_coordinates)):
            horizontal_distance = abs(red_x_coordinates[i][0] - red_x_coordinates[n][0]) + 1
            vertical_distance = abs(red_x_coordinates[i][1] - red_x_coordinates[n][1]) + 1

            area = horizontal_distance * vertical_distance
            # print(f"area is x: {horizontal_distance} * y: {vertical_distance} = {area}")
            if area > largest_area:
                largest_area = area
        
    print(f"p1: {largest_area}")


def solve_part_two():
    red_sq_coordinates = parse_input(EXAMPLE_INPUT)

    largest_area = 0

    grid_coordinates = {
        "X": red_sq_coordinates[0][0],
        "-X": red_sq_coordinates[0][0],
        "Y": red_sq_coordinates[0][1],
        "-Y": red_sq_coordinates[0][1]
    }

    for i in range(1, len(red_sq_coordinates)):
        x = red_sq_coordinates[i][0]
        y = red_sq_coordinates[i][1]

        if x > grid_coordinates.get("X"):
            grid_coordinates["X"] = x
        elif x < grid_coordinates.get("-X"):
            grid_coordinates["-X"] = x

        if y > grid_coordinates.get("Y"):
            grid_coordinates["Y"] = y
        elif y < grid_coordinates.get("-Y"):
            grid_coordinates["-Y"] = y

    grid = 


def main():
    solve_part_one()


if __name__ == "__main__":
    main()