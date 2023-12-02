"""
Advent-of-Code 2023: Day 1 / Part 1
"""

SUM = 0

with open("input", "r", encoding="UTF8") as file:
    for line in file:
        digits = [c for c in line if c.isdigit()]
        SUM += int(digits[0] + digits[-1])

    print(SUM)
