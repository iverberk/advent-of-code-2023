"""
Advent-of-Code 2023: Day 3 / Part 2
"""

import operator
from collections import defaultdict

MAX_X, MAX_Y = 140, 140
SUM = 0

GEAR = "*"
DELTAS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
NON_PART = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

schematic = defaultdict(lambda: ".")
gears = defaultdict(list)

with open("input", "r", encoding="UTF8") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            schematic[(x, y)] = c

for y in range(0, MAX_Y):
    NUMBER = ""
    PART = False
    surrounding_gears = set()
    for x in range(0, MAX_X):
        # If we are not tracking a number, clear the surrounding_gears.
        if not NUMBER:
            surrounding_gears = set()

        if schematic[(x, y)].isdigit():
            NUMBER += schematic[(x, y)]

            for delta in DELTAS:
                pos = tuple(map(operator.add, (x, y), delta))
                if schematic[pos] not in NON_PART:
                    PART = True

                    # Store this gear position in the set of surround gears.
                    if schematic[pos] == GEAR:
                        surrounding_gears.add(pos)

            # Check if this is the last character in the line, and thereby
            # the end of the number. No need to clear the PART and NUMBER
            # variables because we are moving to the next line, which triggers
            # a reset of those variables.
            if x + 1 == MAX_X:
                if PART:
                    # Store the number in all the gears that surround it.
                    for gear in surrounding_gears:
                        gears[gear].append(int(NUMBER))

        elif NUMBER:
            if PART:
                # Store the number in all the gears that surround it.
                for gear in surrounding_gears:
                    gears[gear].append(int(NUMBER))

            PART = False
            NUMBER = ""

# Iterate over all the gears numbers.
for numbers in gears.values():
    if len(numbers) == 2:
        SUM += numbers[0] * numbers[1]

print(SUM)
