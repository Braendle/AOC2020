#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 9 (https://adventofcode.com/2020/day/9)
"""

from itertools import combinations
from pathlib import Path

from more_itertools import windowed, first_true
from more_itertools.more import first


# ======= Helper Functions/Classes ======= #
def windowed_sub(it, min_len=2):
    for s in range(len(data)):
        for e in range(s + min_len, len(it) + 1):
            yield it[s:e]


def get_first_wrong(data, N=25):
    for check_pos, prev_vals in enumerate(windowed(data, N), N):
        for comb in combinations(prev_vals, 2):
            if sum(comb) == data[check_pos]:
                break
        else:
            return data[check_pos]


# ============= Input Data ============= #
raw_data = Path("./inputs/09/input.txt").read_text()
data = [int(x) for x in raw_data.splitlines()]

# =============== PART 1 =============== #
res1 = get_first_wrong(data)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
valid_comb = first_true(windowed_sub(data), pred=lambda x: sum(x) == res1)
res2 = min(valid_comb) + max(valid_comb)
print(f"Result of Part 2: {res2}")
