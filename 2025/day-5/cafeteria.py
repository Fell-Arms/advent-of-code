# https://adventofcode.com/2025/day/5

import timeit

INPUT_FILE = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    fresh_ingredient_id_ranges = []
    available_ingredients = []

    separator_hit = False

    with open(input_path) as f:
        for line in f:
            # print(line)
            line = line.strip()
            if line == '':
                separator_hit = True
                continue

            if not separator_hit and line != '':
                range = line.split('-')
                # print(range)
                fresh_ingredient_id_ranges.append((int(range[0]), int(range[1])))
            elif separator_hit and line != '':
                available_ingredients.append(int(line))

    return fresh_ingredient_id_ranges, available_ingredients


def main():

    # solve_part_one()

    fresh_ingredient_id_ranges, available_ingredients = parse_input(INPUT_FILE)
    fresh_ingredient_list = []
    fresh_ingredient_ids = []
    total_fresh_ingredient_ids = 0


    for id_range in fresh_ingredient_id_ranges:
        for value in range(id_range[0], id_range[1]+1):
            if value not in fresh_ingredient_ids:
                fresh_ingredient_ids.append(value)
            total_fresh_ingredient_ids += 1

    print(total_fresh_ingredient_ids)


def solve_part_one():
    fresh_ingredient_id_ranges, available_ingredients = parse_input(INPUT_FILE)
    fresh_ingredient_list = []


    for ingredient in available_ingredients:
        for id_range in fresh_ingredient_id_ranges:
            if ingredient in range(id_range[0], id_range[1] +1):
                fresh_ingredient_list.append(ingredient)
                break

    print(len(fresh_ingredient_list))



if __name__ == "__main__":
    main()