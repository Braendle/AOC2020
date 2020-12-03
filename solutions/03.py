#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 3 (https://adventofcode.com/2020/day/3)
"""

import numpy as np
from itertools import count


# ======= Helper Functions/Classes ======= #
def walk(data: np.array, right_step: int, down_step: int):
    for i_row, i_col in zip(range(0, data.shape[0], down_step), count(0, right_step)):
        yield data[i_row, i_col % data.shape[1]]


# ============= Input Data ============= #
with open("./inputs/03/input.txt") as h_file:
    data = [[x == '#' for x in line] for line in h_file.read().splitlines()]
    data = np.array(data)

# =============== PART 1 =============== #
res1 = sum(walk(data, 3, 1))
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
moves = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

res2 = np.prod([sum(walk(data, m[0], m[1])) for m in moves])
print(f"Result of Part 2: {res2}")
