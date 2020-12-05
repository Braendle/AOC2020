#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 5 (https://adventofcode.com/2020/day/5)
"""

from pathlib import Path

from more_itertools import consecutive_groups

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
raw_data = Path("./inputs/05/input.txt").read_text()
data = [x for x in raw_data.splitlines()]

# =============== PART 1 =============== #
ids = [int(d.translate(d.maketrans("FBLR", "0101")), 2) for d in data]
res1 = max(ids)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
missing_id = list(list(x)[0] for x in consecutive_groups(sorted(ids)))[1] - 1
res2 = missing_id
print(f"Result of Part 2: {res2}")
