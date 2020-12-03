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
data = []
with open("./inputs/03/input.txt") as h_file:
    for line in h_file.readlines():
        data.append([x == '#' for x in line.strip()])

data = np.array(data)

# =============== PART 1 =============== #
res1 = sum(walk(data, 3, 1))
print("Result of Part 1: {}".format(res1))

# =============== PART 2 =============== #
moves = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

res2 = np.prod([sum(walk(data, m[0], m[1])) for m in moves])
print("Result of Part 2: {}".format(res2))