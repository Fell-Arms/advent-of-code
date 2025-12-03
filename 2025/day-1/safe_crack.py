# https://adventofcode.com/2025/day/1

import io

INPUT_PATH = "./input.txt"
SAFE_START = 50

def parse_input(input: str, is_path: bool = False):
    instructions = []
    if is_path:
        with open(input) as f:
            for line in f:
                if line:
                    instructions.append(line)
    else:
        "foobar"

    return instructions


def main(input = None):

    instructions = None
    current_safe_number = SAFE_START
    previous_safe_number = None
    safe_code = 0
    clicks_zero = 0

    if input is not None:
        instructions = parse_input(input)
    else:
        instructions = parse_input(INPUT_PATH, True)

    for step in instructions:
        direction = step[0]
        turn_number = int(step[1:]) 

        if turn_number > 99:
            clicks_zero += turn_number // 100

        turn_number = turn_number % 100

        temporary_click = 0

        if direction == "L":
            current_safe_number -= turn_number
        elif direction == "R":
            current_safe_number += turn_number

        if current_safe_number > 99: # if hits 100, becomes 0
            current_safe_number = current_safe_number % 100
            temporary_click = 1
        elif current_safe_number < 0:
            current_safe_number = 100 - (current_safe_number * -1)
            if previous_safe_number != 0:
                temporary_click = 1

        if current_safe_number == 0:
            safe_code += 1
            clicks_zero += 1
        else: 
            clicks_zero += temporary_click

        previous_safe_number = current_safe_number


    print(clicks_zero)


if __name__ == "__main__":
    main()