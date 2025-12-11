# https://adventofcode.com/2025/day/10

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    
    instruction_manual = []

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            instruction_manual.append(line)

    return instruction_manual


def solve_part_one():
    manual = parse_input(EXAMPLE_INPUT)

    # each button if pressed will only press once due to redundancy

    for instruction in manual:
        details: str = instruction.split(" ")
        from pprint import pp
        pp(details)

        light_diagram = details[0]
        lights = []
        # must_light_up = []
        for i in range(1, len(light_diagram) -1):
            lights.append(light_diagram[i] == "#")  # Should this index be lit or not? (Cannot mut strings - using bools)
            # if light_diagram[i] == "#":
            #     must_light_up.append(i)
            
        pp(lights)

        joltage_requirements = details[-1]
        buttons = details[1:-1]
        pp(buttons)





def solve_part_two():
    pass


def main():
    solve_part_one()


if __name__ == "__main__":
    main()