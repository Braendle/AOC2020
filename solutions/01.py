#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 1 (https://adventofcode.com/2020/day/1)
"""

from itertools import permutations

import numpy as np

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
with open("./inputs/01/input.txt") as h_file:
    data = [int(x) for x in h_file.readlines()]

# =============== PART 1 =============== #
for comb in  permutations(data, 2):
    if sum(comb) == 2020:
        res1 = np.prod(comb)
        break
print("Result of Part 1: {}".format(res1))

# =============== PART 2 =============== #
for comb in  permutations(data, 3):
    if sum(comb) == 2020:
        res2 = np.prod(comb)
        break
print("Result of Part 2: {}".format(res2))
