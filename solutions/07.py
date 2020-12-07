#!/usr/bin/env python3

"""Advent of Code 2020
    Solution to Day 7 (https://adventofcode.com/2020/day/7)
"""

import re
from pathlib import Path

import networkx as nx


# ======= Helper Functions/Classes ======= #
def get_num_contains(G, cur_node):
    return 1 + sum(G[cur_node][s]["n_children"]*get_num_contains(G, s) for s in G.successors(cur_node))


# ============= Input Data ============= #
raw_data = Path("./inputs/07/input.txt").read_text()
# Let's try to solve the puzzle by using networkx. Might be easier to do it by hand...
edges = []
for line in raw_data.splitlines():
    p, cs = line.split(" bags contain ")
    if not cs.startswith("no other"):
        for c in cs.split(", "):
            grps = re.match(r"^(\d+) (.+?) bag.{,2}$", c).groups()
            edges.append((p, grps[1], {'n_children': int(grps[0])}))
G = nx.DiGraph(edges)


# =============== PART 1 =============== #
res1 = len(nx.shortest_path(G, target='shiny gold')) - 1
print(f"Result of Part 1: {res1}")

# =============== PART 2 =============== #
res2 = get_num_contains(G, "shiny gold") - 1
print(f"Result of Part 2: {res2}")
