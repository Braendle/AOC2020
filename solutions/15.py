#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 15 (https://adventofcode.com/2020/day/15)
"""

from itertools import count
from pathlib import Path

from more_itertools import nth


# ======= Helper Functions/Classes ======= #
def speek(start_nums):
    seen = {x: i for i, x in enumerate(start_nums)}
    for n in start_nums:
        yield n
    prev = start_nums[-1]
    for i in count(len(start_nums)):
        if prev in seen:
            new = i - seen[prev] - 1
        else:
            new = 0
        seen[prev] = i-1
        yield new
        prev = new


# ============= Input Data ============= #
raw_data = Path("./inputs/15/input.txt").read_text().strip()
start_nums = [int(x) for x in raw_data.split(",")]

# =============== PART 1 =============== #
res1 = nth(speek(start_nums), 2020-1)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
# brute-force is sufficient
res2 = nth(speek(start_nums), 30_000_000-1)
print(f"Result of Part 2: {res2}")
