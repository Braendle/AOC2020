#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 18 (https://adventofcode.com/2020/day/18)
"""

from pathlib import Path

import tatsu

# ======= Helper Functions/Classes ======= #
PARSER1 = tatsu.compile(r"""
    start          = line $;
    line           = /\n/.{expression}+;
    expression     = addition | multiplication | factor;
    addition       = left:expression op:'+' ~ right:factor;
    multiplication = left:expression op:'*' ~ right:factor;
    factor         = '('~ @:expression ')' | number;
    number         = /\d+/;
""")

PARSER2 = tatsu.compile(r"""
    start          = line $;
    line           = /\n/.{expression}+;
    expression     = multiplication | term;
    multiplication = left:expression op:'*' ~ right:term ;
    term           = addition | factor;
    addition       = left:term op:'+' ~ right:factor ;
    factor         = '('~ @:expression ')' | number;
    number         = /\d+/;
""")


class Semantics:
    def line(self, ast):
        return sum(ast)

    def number(self, ast):
        return int(ast)

    def addition(self, ast):
        return ast.left + ast.right

    def multiplication(self, ast):
        return ast.left * ast.right


# ============= Input Data ============= #
raw_data = Path("./inputs/18/input.txt").read_text().strip()
exprs = raw_data.splitlines()

# =============== PART 1 =============== #
res1 = PARSER1.parse(raw_data, semantics=Semantics())
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
res2 = PARSER2.parse(raw_data, semantics=Semantics())
print(f"Result of Part 2: {res2}")
