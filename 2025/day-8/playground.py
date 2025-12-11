# https://adventofcode.com/2025/day/8

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    
    junction_box_coordinates = []

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            coordinates = line.split(",")
            junction_box_coordinates.append({
                "X": int(coordinates[0]),
                "Y": int(coordinates[1]),
                "Z": int(coordinates[2])
            })

    return junction_box_coordinates


def solve_part_one():
    coordinates = parse_input(EXAMPLE_INPUT)

    from pprint import pp
    pp(coordinates)

    # In three dimensions, for points given by their Cartesian coordinates, the distance is: 
    # https://en.wikipedia.org/wiki/Euclidean_distance#Higher_dimensions

    used_indices = []
    junction_box_pairs = []  # []
    junction_box_groups = {}  # key: [1,2,3]

    # try list of sets


    for i in range(0, len(coordinates)):
        if i in used_indices:
            continue

        current_x = coordinates[i].get("X")
        current_y = coordinates[i].get("Y")
        current_z = coordinates[i].get("Z")

        shortest_distance_index = None
        shortest_prior_distance = None

        for n in range(0, len(coordinates)):
            if n == i:
                continue
            elif n in used_indices:
                continue

            compare_x = coordinates[n].get("X")
            compare_y = coordinates[n].get("Y")
            compare_z = coordinates[n].get("Z")

            distance_x = (current_x - compare_x)**2
            distance_y = (current_y - compare_y)**2
            distance_z = (current_z - compare_z)**2

            distance = distance_x + distance_y + distance_z

            if distance < shortest_prior_distance:
                shortest_distance_index = n
                shortest_prior_distance = distance

            elif shortest_distance_index == None and shortest_prior_distance == None:
                shortest_distance_index = n
                continue

        used_indices.append[i]
        used_indices.append[shortest_distance_index]


def main():
    solve_part_one()


if __name__ == "__main__":
    main()


def old_solve_part_one():

    coordinates = parse_input(EXAMPLE_INPUT)

    from pprint import pp
    pp(coordinates)

    # In three dimensions, for points given by their Cartesian coordinates, the distance is: 
    # https://en.wikipedia.org/wiki/Euclidean_distance#Higher_dimensions

    used_indices = []
    junction_box_pairs = []

    for i in range(0, len(coordinates)):
        if i in used_indices:
            continue

        current_x = coordinates[i].get("X")
        current_y = coordinates[i].get("Y")
        current_z = coordinates[i].get("Z")

        shortest_distance_index = None
        shortest_prior_distance = None

        for n in range(i+1, len(coordinates)):
            if n in used_indices:
                continue

            compare_x = coordinates[n].get("X")
            compare_y = coordinates[n].get("Y")
            compare_z = coordinates[n].get("Z")

            distance_x = (current_x - compare_x)**2
            distance_y = (current_y - compare_y)**2
            distance_z = (current_z - compare_z)**2

            distance = distance_x + distance_y + distance_z

            if distance < shortest_prior_distance:
                shortest_distance_index = n
                shortest_prior_distance = distance
            elif shortest_distance_index == None and shortest_prior_distance == None:
                shortest_distance_index = n
                continue

        used_indices.append[i]
        used_indices.append[shortest_distance_index]