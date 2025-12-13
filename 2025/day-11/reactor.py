# https://adventofcode.com/2025/day/11

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    
    instructions = []

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            instructions.append(line)

    return instructions


def solve_part_one():
    instructions = parse_input(EXAMPLE_INPUT)
    graph_diagram = {}

    
    for line in instructions:
        points = line.split(" ")
        points[0] = points[0].strip(":")

        graph_diagram[points[0]] = {}


        for i in range(1, len(points)):
            graph_diagram[points[0]][]
        


def solve_part_two():
    pass


def main():
    solve_part_one()


if __name__ == "__main__":
    main()