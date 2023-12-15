"""
Advent-of-Code 2023: Day 15 / Part 1
"""

sequence = open("input").readline().strip().split(",")


def HASH(inp):
    current_value = 0
    for c in inp:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    return current_value


s = 0
for step in sequence:
    s += HASH(step)

print(s)
