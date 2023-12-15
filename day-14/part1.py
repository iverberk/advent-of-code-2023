"""
Advent-of-Code 2023: Day 14 / Part 1
"""

# pylint: disable=C0103

platform = []
with open("test-input", "r", encoding="UTF8") as file:
    for line in file:
        platform.append(list(line.strip()))

# Rotate 90 degrees clockwise for horizontal processing.
platform = list(zip(*platform[::-1]))

total_load = 0
for row in platform:
    top = len(platform)
    for idx, c in enumerate(reversed(row)):
        if c == "O":
            total_load += top
            top -= 1

        if c == "#":
            top = len(platform) - idx - 1

print(total_load)
