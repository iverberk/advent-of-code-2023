"""
Advent-of-Code 2023: Day 8 / Part 1
"""

import re
import sys

instructions = ""
network = {}
with open("input", "r", encoding="UTF8") as file:
    instructions = file.readline().strip()

    for line in file:
        line = line.strip()

        if line:
            m = re.match(r"(.*) = \((.*), (.*)\)", line)
            network[m.group(1)] = (m.group(2), m.group(3))

steps = 0
location = "AAA"

while True:
    for instruction in instructions:
        location = network[location][0] if instruction == "L" else network[location][1]
        steps += 1

        if location == "ZZZ":
            print(steps)
            sys.exit()
