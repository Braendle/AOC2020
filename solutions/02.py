#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 2 (https://adventofcode.com/2020/day/2)
"""

from common import parselines

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
with open("./inputs/02/input.txt") as h_file:
    data = parselines("{l:d}-{h:d} {c}: {s}", h_file.read())

# =============== PART 1 =============== #
cnt = sum(d["l"] <= d["s"].count(d["c"]) <= d["h"] for d in data)
res1 = cnt
print("Result of Part 1: {}".format(res1))

# =============== PART 2 =============== #
cnt = sum((d["s"][d["l"]-1] == d["c"]) ^ (d["s"][d["h"]-1] == d["c"]) for d in data)
res2 = cnt
print("Result of Part 2: {}".format(res2))
