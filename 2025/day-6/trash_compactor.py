# https://adventofcode.com/2025/day/6

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    
    math_homework = []

    with open(input_path) as f:
        for line in f:
            # print(line)
            line = line.strip()

            math_homework.append(line.split())

    return math_homework


def solve_part_one(math_homework):
    math_homework = parse_input(INPUT_FILE)
    operation_index = len(math_homework) - 1
    last_number = operation_index - 1

    numbers_for_operation = []
    operation = ''
    grand_total = 0

    for i in range(0, len(math_homework[0])):
        numbers_for_operation.clear()
        operation = ''
        for n in range(0, len(math_homework)):
            if n != operation_index:
                numbers_for_operation.append(int(math_homework[n][i]))
            else:
                operation = math_homework[n][i]
                total = 0
                for number in range(0, len(numbers_for_operation)):
                    if number == 0:
                        total = numbers_for_operation[number]
                    else:
                        if operation == '+':
                            total += numbers_for_operation[number]
                        if operation == '*':
                            total *= numbers_for_operation[number]
                        elif operation == '':
                            print("unassigned operation")

                grand_total += total

    print(f"p1: {grand_total}")


def solve_part_two(math_homework):
    math_homework = parse_input(EXAMPLE_INPUT)
    operation_index = len(math_homework) - 1

    numbers_for_operation = []
    operation = ''
    grand_total = 0

    # number of columns e.g. however many parts of the homework to solve
    for i in range(0, len(math_homework[0])):
        numbers_for_operation.clear()
        operation = ''

        # number of rows e.g. however many numbers to use in compute/homework
        for n in range(0, len(math_homework)):
            if n != operation_index:

                for char in range (0, len(math_homework[n][i])):
                    target_index = len(math_homework[n][i]) - (char + 1)
                    try:
                        numbers_for_operation[char] = f"{numbers_for_operation[char]}{math_homework[n][i][target_index]}" 
                    except:
                        numbers_for_operation.append(math_homework[n][i][target_index])
            else:
                operation = math_homework[n][i]
                total = 0
                for number in range(0, len(numbers_for_operation)):
                    print(numbers_for_operation[number])
                    if number == 0:
                        total = int(numbers_for_operation[number])
                    else:
                        if operation == '+':
                            total += int(numbers_for_operation[number])
                        if operation == '*':
                            total *= int(numbers_for_operation[number])
                        elif operation == '':
                            print("unassigned operation")

                grand_total += total

    print(f"p2: {grand_total}")


def main():
    math_homework = parse_input(INPUT_FILE)
    example_homework = parse_input(EXAMPLE_INPUT)

    solve_part_one(math_homework)
    solve_part_two(example_homework)
                    


if __name__ == "__main__":
    main()