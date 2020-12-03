#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 2 (https://adventofcode.com/2020/day/2)
"""

from pathlib import Path

from common import parselines

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
raw_data = Path("./inputs/02/input.txt").read_text()
data = parselines("{l:d}-{h:d} {c}: {s}", raw_data)

# =============== PART 1 =============== #
res1 = sum(d["l"] <= d["s"].count(d["c"]) <= d["h"] for d in data)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
res2 = sum((d["s"][d["l"]-1] == d["c"]) ^ (d["s"][d["h"]-1] == d["c"]) for d in data)
print(f"Result of Part 2: {res2}")
