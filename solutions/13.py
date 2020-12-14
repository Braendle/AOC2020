#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 13 (https://adventofcode.com/2020/day/13)
"""

from itertools import count
from pathlib import Path

# ======= Helper Functions/Classes ======= #


# ============= Input Data ============= #
raw_data = Path("./inputs/13/input.txt").read_text().strip()
lines = raw_data.splitlines()
t_min = int(lines[0])
bus_ids = [int(i) for i in lines[1].split(",") if i != "x"]

# =============== PART 1 =============== #
t_diffs = {}
for bus_id in bus_ids:
    t_diff = bus_id - (t_min % bus_id)
    t_diffs[bus_id] = t_diff

min_id = min(t_diffs, key=t_diffs.get)

res1 = min_id * t_diffs[min_id]
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
bus_remainders = [(int(n), i) for i, n in enumerate(lines[1].split(",")) if n != "x"]
bus_remainders.sort(reverse=True)
v = 0
step = 1
for bus, offs in bus_remainders:
    for i in count(v, step):
        if (i + offs) % bus == 0:
            v = i
            step *= bus
            break

res2 = v
print(f"Result of Part 2: {res2}")
