# https://adventofcode.com/2025/day/11

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

shapes = {
    "0": [["#.#"],["###"],["#.#"]],
    "1": [["#.."],["##."],["###"]],
    "2": [[".##"],["###"],["#.#"]],
    "3": [["###"],["#.#"],["#.#"]],
    "4": [["##."],["##."],["###"]],
    "5": [[".##"],["##."],["#.."]],
}

def parse_input(input_path: str):
    
    instructions = []

    with open(input_path) as f:
        for line in f:
            if line is not None:
                instructions.append(line)

    return instructions


def solve_part_one():
    manual = parse_input(INPUT_FILE)

    trees_fitting_presents = 0
    trees_not_fitting_presents = 0

    for line in manual:
        instructions = line.split(":")
        grid = int(instructions[0][0:2]) * int(instructions[0][3:5])

        # pp(instructions[1])
        shapes_to_fit = instructions[1].strip().split(" ")
        # pp(shapes_to_fit)

        shapes_grid_can_fit = grid // 9

        total_shapes = 0
        
        for shapes in shapes_to_fit:
            total_shapes += int(shapes)
            
        if total_shapes <= shapes_grid_can_fit:
            trees_fitting_presents += 1
        else:
            trees_not_fitting_presents += 1


    print(f"trees that can fit presents: {trees_fitting_presents}")
    print(f"trees that cannot fit presents: {trees_not_fitting_presents}")


def solve_part_two():
    pass


def main():
    solve_part_one()


if __name__ == "__main__":
    main()