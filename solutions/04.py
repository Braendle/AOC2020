#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 4 (https://adventofcode.com/2020/day/4)
"""

import re
from pathlib import Path

# ======= Helper Functions/Classes ======= #

# ============= Input Data ============= #
raw_data = Path("./inputs/04/input.txt").read_text()
pws = [dict(attr.split(":") for attr in pw_raw.split())
       for pw_raw in raw_data.split("\n\n")]

# =============== PART 1 =============== #
REQ_ATTRS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
pws_valid_fields = [pw for pw in pws if set(pw.keys()) >= REQ_ATTRS]
res1 = len(pws_valid_fields)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
RULES = {
    "byr": lambda v: re.match(r"^\d{4}$", v) and 1920 <= int(v) <= 2002,
    "iyr": lambda v: re.match(r"^\d{4}$", v) and 2010 <= int(v) <= 2020,
    "eyr": lambda v: re.match(r"^\d{4}$", v) and 2020 <= int(v) <= 2030,
    "hgt": lambda v: re.match(r"^(\d+)(cm|in)$", v) and ((v[-2:] == "cm" and 150 <= int(v[:-2]) <= 193) or
                                                         (v[-2:] == "in" and 59 <= int(v[:-2]) <= 76)),
    "hcl": lambda v: re.match(r"^#[0-9a-f]{6}$", v),
    "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda v: re.match(r"^\d{9}$", v),
    "cid": lambda _: True
}
pws_valid_values = [pw for pw in pws_valid_fields if all(RULES[k](v) for k, v in pw.items())]
res2 = len(pws_valid_values)
print(f"Result of Part 2: {res2}")
