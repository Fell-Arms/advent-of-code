# https://adventofcode.com/2025/day/4

import timeit

INPUT_PATH = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    paper_grid = []

    with open(input_path) as f:
        for line in f:
            if line is not None:
                row_line = line.strip()
                row = []
                for char in row_line:
                    row.append(char)
                paper_grid.append(row)
        
    return paper_grid


def solve_part_one(paper_grid):
    free_space_coordinates = []
    accessible_rolls = 0

    search_spaces = 8

    for row in range(0, len(paper_grid)):

        for column in range(0, len(paper_grid[row])):
            row_item = paper_grid[row][column]

            if row_item == '.':
                free_space_coordinates.append((row, column))
                continue
            elif row_item == '@':

                try:
                    "foobar"
                except:
                    "foobar"


def row_item_is_accessible(grid, free_space_coordinates, row, column, search_area = 1):

    item = grid[row]

    items_in_area = 0

    while search_area > 0:




    return True
