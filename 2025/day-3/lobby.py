# https://adventofcode.com/2025/day/3

import timeit

INPUT_PATH = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    battery_banks = []

    with open(input_path) as f:
        for line in f:
            if line is not None:
                battery_banks.append(line.strip())
        
    return battery_banks


def solve_part_one(battery_banks):
    max_joltage_list = []
    max_joltage_sum = 0

    for index in range(0, len(battery_banks)):
        battery_bank = battery_banks[index]
        print(battery_bank)

        num1 = 0
        num2 = 0

        num1_change_index = 0
        num2_handled = True

        for char in range(0, len(battery_bank)):
                
            battery_joltage = int(battery_bank[char])
            if num1 < battery_joltage and char != len(battery_bank) - 1:
                num1 = battery_joltage
                num1_change_index = char
                num2_handled = False
                continue

            if num2 < battery_joltage:
                num2 = battery_joltage
                num2_handled = True
            elif num1_change_index < char and not num2_handled:
                num2 = battery_joltage
                num2_handled = True


        largest_joltage = int(f"{str(num1)}{str(num2)}")
        max_joltage_list.append(largest_joltage)
        max_joltage_sum += largest_joltage

    print(max_joltage_list)

    return max_joltage_sum


def solve_part_two(battery_banks):
    max_joltage_list = []
    max_joltage_sum = 0

    for index in range(0, len(battery_banks)):
        battery_bank = battery_banks[index]
        # print(battery_bank)

        max_joltage_builder = []
        num1 = 0
        num2 = 0

        num1_change_index = 0
        num2_handled = True

        for char in range(0, len(battery_bank)):
                
            battery_joltage = int(battery_bank[char])
            if num1 < battery_joltage and char != len(battery_bank) - 1:
                num1 = battery_joltage
                num1_change_index = char
                num2_handled = False
                continue

            if num2 < battery_joltage:
                num2 = battery_joltage
                num2_handled = True
            elif num1_change_index < char and not num2_handled:
                num2 = battery_joltage
                num2_handled = True


        largest_joltage = int(f"{str(num1)}{str(num2)}")
        max_joltage_list.append(largest_joltage)
        max_joltage_sum += largest_joltage

    print(max_joltage_list)

    return max_joltage_sum


def main():

    battery_banks = parse_input(INPUT_PATH)
    part_one_result = solve_part_one(battery_banks)
    print(part_one_result)


if __name__ == "__main__":
    main()

