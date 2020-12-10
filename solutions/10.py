#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 10 (https://adventofcode.com/2020/day/10)
"""

from collections import Counter
from functools import lru_cache, reduce
from itertools import groupby
from operator import mul
from pathlib import Path

import numpy as np


# ======= Helper Functions/Classes ======= #
@lru_cache(maxsize=None)
def tribonacci(n):
    if (n in range(3)):
        return 0
    elif n == 3:
        return 1
    else:
        return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)


# ============= Input Data ============= #
raw_data = Path("./inputs/10/input.txt").read_text().strip()
data = [int(x) for x in raw_data.split("\n")]

# =============== PART 1 =============== #
data.sort()
diff = np.diff([0] + data + [data[-1]+3])
counts = Counter(diff)
res1 = counts[1] * counts[3]

print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
# For each contiguous series of 1s calculate the tribonacci number of its length and multiply all tribonacci numbers together.
cnt = reduce(mul, (tribonacci(len(list(grp))+3) for d, grp in groupby(diff) if d == 1))
res2 = cnt
print(f"Result of Part 2: {res2}")
