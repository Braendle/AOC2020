#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 8 (https://adventofcode.com/2020/day/8)
"""

from pathlib import Path

from common import parselines


# ======= Helper Functions/Classes ======= #
def run(instrs):
    seen = []
    acc = 0
    ic = 0
    while ic < len(instrs):
        cur_instr = instrs[ic]
        if ic in seen:
            return acc, False
        seen.append(ic)
        if cur_instr['i'] == "acc":
            acc += cur_instr['d']
        elif cur_instr['i'] == "jmp":
            ic += cur_instr['d']
            continue
        ic += 1

    return acc, True


# ============= Input Data ============= #
raw_data = Path("./inputs/08/input.txt").read_text()
instrs = parselines("{i} {d:d}", raw_data)

# =============== PART 1 =============== #
res1, _ = run(instrs)
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
xchg_instr_idxs = [i for i, x in enumerate(instrs) if x['i'] in ['nop', 'jmp']]
for xchg_instr_idx in xchg_instr_idxs:
    instrs[xchg_instr_idx]['i'] = 'nop' if instrs[xchg_instr_idx]['i'] == 'jmp' else 'jmp'
    acc, terminated = run(instrs)
    instrs[xchg_instr_idx]['i'] = 'nop' if instrs[xchg_instr_idx]['i'] == 'jmp' else 'jmp'
    if terminated:
        break

res2 = acc
print(f"Result of Part 2: {res2}")
