#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 12 (https://adventofcode.com/2020/day/12)
"""

from pathlib import Path

import common

# ======= Helper Functions/Classes ======= #


# ============= Input Data ============= #
raw_data = Path("./inputs/12/input.txt").read_text().strip()
data = common.parselines("{instr}{n:d}", raw_data)

# =============== PART 1 =============== #
ship_pos, ship_dir = 0 + 0j, 1 + 0j
for d in data:
    if d['instr'] == "N":
        ship_pos += d['n']*1j
    elif d['instr'] == "S":
        ship_pos -= d['n']*1j
    elif d['instr'] == "E":
        ship_pos += d['n']
    elif d['instr'] == "W":
        ship_pos -= d['n']
    elif d['instr'] == "L":
        ship_dir *= 1j ** (d['n'] // 90)
    elif d['instr'] == "R":
        ship_dir /= 1j ** (d['n'] // 90)
    elif d['instr'] == "F":
        ship_pos += ship_dir * d['n']

res1 = int(abs(ship_pos.real) + abs(ship_pos.imag))
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
ship_pos = 0 + 0j
wp_pos = 10 + 1j
for d in data:
    if d['instr'] == "N":
        wp_pos += d['n']*1j
    elif d['instr'] == "S":
        wp_pos -= d['n']*1j
    elif d['instr'] == "E":
        wp_pos += d['n']
    elif d['instr'] == "W":
        wp_pos -= d['n']
    elif d['instr'] == "L":
        wp_pos = wp_pos * 1j ** (d['n'] // 90)
    elif d['instr'] == "R":
        wp_pos = wp_pos / 1j ** (d['n'] // 90)
    elif d['instr'] == "F":
        ship_pos += wp_pos * d['n']

res2 = int(abs(ship_pos.real) + abs(ship_pos.imag))
print(f"Result of Part 2: {res2}")
