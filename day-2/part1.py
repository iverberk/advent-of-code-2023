"""
Advent-of-Code 2023: Day 2 / Part 1
"""
import re

RED = 12
GREEN = 13
BLUE = 14

SUM = 0

with open("input", "r", encoding="UTF8") as file:
    GAME = 1
    for line in file:
        if (
            all(int(d) <= BLUE for d in re.findall(r"(\d+) blue", line))
            and all(int(d) <= GREEN for d in re.findall(r"(\d+) green", line))
            and all(int(d) <= RED for d in re.findall(r"(\d+) red", line))
        ):
            SUM += GAME
        GAME += 1

    print(SUM)
