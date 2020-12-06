#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 6 (https://adventofcode.com/2020/day/6)
"""

from pathlib import Path

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
raw_data = Path("./inputs/06/input.txt").read_text().strip()
data = [g.split("\n") for g in raw_data.split("\n\n")]

# =============== PART 1 =============== #
cnt = sum(len(set.union(*[set(p) for p in g])) for g in data)
res1 = cnt
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
cnt = sum(len(set.intersection(*[set(p) for p in g])) for g in data)
res2 = cnt
print(f"Result of Part 2: {res2}")
