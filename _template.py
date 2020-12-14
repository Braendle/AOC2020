#!/usr/bin/env python3

"""Advent of Code {year:04d}
    Solution to Day {day} (https://adventofcode.com/{year:04d}/day/{day})
"""

from pathlib import Path

import common

# ======= Helper Functions/Classes ======= #



# ============= Input Data ============= #
raw_data = Path("./inputs/{day:02d}/input.txt").read_text().strip()

lines = raw_data.splitlines()
words = raw_data.split(", ")
ints = [int(x) for x in raw_data.split("\n")]
data = common.parselines("{{number:d}}: {{string}}", raw_data)

# =============== PART 1 =============== #
res1 = None
print(f"Result of Part 1: {{res1}}")

# =============== PART 2 =============== #
res2 = None
print(f"Result of Part 2: {{res2}}")
