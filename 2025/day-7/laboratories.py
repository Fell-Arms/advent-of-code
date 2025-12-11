# https://adventofcode.com/2025/day/7

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    
    diagram = []

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            diagram.append(list(line))

    return diagram


def solve_part_one():

    diagram = parse_input(INPUT_FILE)
    number_splits = 0

    for char in range(0, len(diagram[0])):
        if diagram[0][char] == "S":
            diagram[1][char] = "|"
            print("hit S")

    for i in range(1, len(diagram)):
        for char in range(0, len(diagram[i])):
            if diagram[i][char] == "^":
                if  i-1 >= 0 and diagram[i-1][char] == "|":
                    number_splits += 1

                    if char-1 >= 0:
                        diagram[i][char-1] = "|"

                    if char+1 < len(diagram[i]):
                        diagram[i][char+1] = "|"
            elif diagram[i][char] == ".":
                if i-1 >=0 and diagram[i-1][char] == "|":
                    diagram[i][char] = "|"

    for line in diagram:
        print(line)

    print(f"p1 splits: {number_splits}")


def main():
    solve_part_one()


if __name__ == "__main__":
    main()



def old_solve_part_one():
    # refactored because buggy & bad

    diagram = parse_input(INPUT_FILE)
    number_splits = 0

    for char in range(0, len(diagram[0])):
        if diagram[0][char] == "S":
            diagram[1][char] = "|"
            print("hit S")

    for i in range(1, len(diagram)):
        if i % 2 == 0:
            for char in range(0, len(diagram[i])):
                try:
                    if diagram[i][char] == "^":
                        if diagram[i-1][char] == "|":
                            if char-1 >= 0:
                                diagram[i][char-1] = "|"
                            elif char+1 < len(diagram[i]):
                                diagram[i][char+1] = "|"
                            number_splits += 1
                            if i+1 < len(diagram):
                                diagram[i+1][char-1] = "|"
                                diagram [i+1][char+1] = "|"
                    elif diagram[i][char] == ".":
                        if diagram[i-1][char] == "|":
                            diagram[i][char] == "|"
                except:  # catch out of bounds (should probably just add a conditional)
                    continue
        elif i % 2 == 1:
            for char in range(0, len(diagram[i])):
                if diagram[i][char] == "^":
                    print("found splitter - shouldn't have")

                if diagram[i][char] == "|" or (diagram[i][char -1] == "|" and char != 0):
                    try:
                        if diagram[i+1][char] == "^":
                            continue
                        elif diagram[i+1][char] == ".":
                            diagram[i+1][char] = "|"
                    except:  # catch out of bounds (should probably just add a conditional)
                        continue

    for line in diagram:
        print(line)

    print(f"p1 splits: {number_splits}")