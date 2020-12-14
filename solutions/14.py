#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 14 (https://adventofcode.com/2020/day/14)
"""

from pathlib import Path

from parse import parse


# ======= Helper Functions/Classes ======= #
def get_all_addrs(remain: list, cur):
    if len(remain) == 0:
        yield cur
    else:
        if remain[-1] == "X":
            yield from get_all_addrs(remain[:-1], cur+["0"])
            yield from get_all_addrs(remain[:-1], cur+["1"])
        else:
            yield from get_all_addrs(remain[:-1], cur+[remain[-1]])


# ============= Input Data ============= #
raw_data = Path("./inputs/14/input.txt").read_text().strip()

# =============== PART 1 =============== #
mask = "X"*36
mem = {}
for line in raw_data.splitlines():
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
    else:
        addr, val = parse("mem[{:d}] = {:d}", line)
        new_val = list("{:036b}".format(val))
        for i, c in enumerate(mask):
            if c != "X":
                new_val[i] = c
        mem[addr] = int("".join(new_val), 2)

res1 = sum(val for val in mem.values())
print(f"Result of Part 1: {res1}")


# =============== PART 2 =============== #
mask = "X"*36
mem = {}
for line in raw_data.splitlines():
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
    else:
        addr, val = parse("mem[{:d}] = {:d}", line)
        new_addr = list("{:036b}".format(addr))
        for i, c in enumerate(mask):
            if c != "0":
                new_addr[i] = mask[i]

        for addr in get_all_addrs(new_addr, []):
            mem[int("".join(addr), 2)] = val
res2 = sum(val for val in mem.values())
print(f"Result of Part 2: {res2}")
