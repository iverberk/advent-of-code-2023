"""
Advent-of-Code 2023: Day 3 / Part 1
"""

import operator
from collections import defaultdict

MAX_X, MAX_Y = 140, 140
SUM = 0

DELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
NON_PART = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

schematic = defaultdict(lambda: ".")

with open("input", "r", encoding="UTF8") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            schematic[(x, y)] = c

for y in range(0, MAX_Y):
    NUMBER = ""
    PART = False
    for x in range(0, MAX_X):
        if schematic[(x, y)].isdigit():
            NUMBER += schematic[(x, y)]

            for delta in DELTAS:
                if schematic[tuple(map(operator.add, (x, y), delta))] not in NON_PART:
                    PART = True

            # Check if this is the last character in the line.
            if x + 1 == MAX_X:
                if PART:
                    SUM += int(NUMBER)

        elif NUMBER:
            if PART:
                SUM += int(NUMBER)

            PART = False
            NUMBER = ""

print(SUM)
