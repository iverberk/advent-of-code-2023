"""
Advent-of-Code 2023: Day 2 / Part 2
"""
import re

SUM = 0

with open("input", "r", encoding="UTF8") as file:
    for line in file:
        blue = max(int(d) for d in re.findall(r"(\d+) blue", line))
        green = max(int(d) for d in re.findall(r"(\d+) green", line))
        red = max(int(d) for d in re.findall(r"(\d+) red", line))

        SUM += blue * green * red

    print(SUM)
