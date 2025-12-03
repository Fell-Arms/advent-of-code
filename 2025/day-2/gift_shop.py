# https://adventofcode.com/2025/day/2

import timeit

INPUT_PATH = "./input.txt"
EXAMPLE_INPUT = "./example_input.txt"

def parse_input(input_path: str):
    id_range_list = []

    with open(input_path) as f:
        actual_line_count = 0
        expected_line_count = 1
        for line in f:
            if line is not None:
                id_range_list = line.split(sep=",")
                actual_line_count += 1
        
        if actual_line_count != expected_line_count:
            print(f"unlucky, exiting. {actual_line_count} != {expected_line_count}")
            exit()

    return id_range_list


def same_digit_ranges(id_range_list):
    all_same = True

    for id_range in id_range_list:
        search_range = id_range.split("-")

        if len(search_range[0]) != len(search_range[1]):
            all_same = False

    return all_same


def solve_part_one(id_range_list):
    start = timeit.default_timer()

    result = 0

    for id_range in id_range_list:
        search_range = id_range.split("-")

        range_start_odd_digits = (len(search_range[0]) % 2 == 1)
        range_end_odd_digits = (len(search_range[1]) % 2 == 1)
        same_total_digits = (len(search_range[0]) == len(search_range[1]))

        # patterns only occur with even numbers of digits
        if range_start_odd_digits:
            if same_total_digits:
                continue

        forward = int(search_range[0])
        end = int(search_range[1])

        while forward <= end:
            forward_str = str(forward)
            forward_len = len(forward_str)

            # skip odd digits
            if forward_len % 2 == 1:
                forward = 10**forward_len
                continue

            middle = int(forward_len/2)

            if forward_str[middle:] == forward_str[:middle]:
                result += forward
                print(f"Adding invalid id {forward} to result. New result: {result}")

            forward += 1

    print(f"Part 1 result: {result}")

    stop = timeit.default_timer()
    print('Time: ', stop - start)  


def solve_part_two(id_range_list):
    result = 0

    for id_range in id_range_list:
        search_range = id_range.split("-")

        forward = int(search_range[0])
        end = int(search_range[1])

        while forward <= end:
            forward_str = str(forward)
            forward_len = len(forward_str)

            pattern_current = 1

            while pattern_current <= forward_len // 2:
                pattern = forward_str[:pattern_current]
                check_pattern = pattern * (forward_len // pattern_current)

                if check_pattern == forward_str:
                    result += forward
                    print(f"Found match: \nPattern {pattern} repeats in {forward_str}")
                    print(f"Adding invalid id {forward} to result. New result: {result} \n")
                    break

                pattern_current += 1

            forward +=1

    print(f"part 2 result: {result}")


def main():

    id_range_list = parse_input(INPUT_PATH)

    if same_digit_ranges(id_range_list):
        print(f"Ranges are limited to X digits")
    else:
        print(f"ranges are not limited to X digits")    

    solve_part_one(id_range_list)

    solve_part_two(id_range_list)


if __name__ == "__main__":
    main()