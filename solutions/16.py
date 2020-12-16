#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 16 (https://adventofcode.com/2020/day/16)
"""

from collections import defaultdict
from functools import reduce
from operator import mul
from pathlib import Path

from parse import parse

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
field_ranges = {}
raw_data = Path("./inputs/16/input.txt").read_text().strip()
blocks = raw_data.split("\n\n")
for line in blocks[0].splitlines():
    field, l1, h1, l2, h2 = parse("{}: {:d}-{:d} or {:d}-{:d}", line)
    field_ranges[field] = (l1, h1, l2, h2)
my_ticket = [int(x) for x in blocks[1].splitlines()[1].split(",")]
nearby_tickets = [[int(x) for x in line.split(",")] for line in blocks[2].splitlines()[1:]]

# =============== PART 1 =============== #
invalid_vals = []
valid_tickets = []
for nt in nearby_tickets:
    for n in nt:
        for l1, h1, l2, h2 in field_ranges.values():
            if l1 <= n <= h1 or l2 <= n <= h2:
                break
        else:
            invalid_vals.append(n)
            break
    else:
        valid_tickets.append(nt)
valid_tickets.append(my_ticket)

res1 = sum(invalid_vals)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
candidates = defaultdict(list)
for i_field in range(len(valid_tickets[0])):
    for field_name, (l1, h1, l2, h2) in field_ranges.items():
        valid = True
        for vt in valid_tickets:
            if not (l1 <= vt[i_field] <= h1 or l2 <= vt[i_field] <= h2):
                valid = False
                break
        else:
            candidates[i_field].append(field_name)

field_mapping = {}
while len(candidates) > 0:
    for i_field, field_names in candidates.items():
        if len(field_names) == 1:
            field_mapping[i_field] = field_names[0]
            candidates.pop(i_field)
            for j_field in candidates:
                candidates[j_field].remove(field_names[0])
            break
    else:
        raise Exception("no singelton available")

res2 = reduce(mul, (my_ticket[i] for i, f in field_mapping.items() if f.startswith("departure")), 1)
print(f"Result of Part 2: {res2}")
