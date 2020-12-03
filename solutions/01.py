#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 1 (https://adventofcode.com/2020/day/1)
"""

from itertools import permutations
from pathlib import Path

import numpy as np
from more_itertools import first_true

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
raw_data = Path("./inputs/01/input.txt").read_text()
data = [int(x) for x in raw_data.splitlines()]

# =============== PART 1 =============== #
res1 = np.prod(first_true(permutations(data, 2), pred=lambda comb: sum(comb) == 2020))
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
res2 = np.prod(first_true(permutations(data, 3), pred=lambda comb: sum(comb) == 2020))
print(f"Result of Part 2: {res2}")
