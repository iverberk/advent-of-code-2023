"""
Advent-of-Code 2023: Day 14 / Part 2
"""

# pylint: disable=C0103

platform = []
with open("input", "r", encoding="UTF8") as file:
    for line in file:
        platform.append(list(line.strip()))


def tilt(platform):
    new_platform = []
    for row in platform:
        right = len(platform) - 1
        new_row = ["#" if c == "#" else "." for c in row]
        for idx, c in enumerate(reversed(row)):
            if c == "O":
                new_row[right] = c
                right -= 1

            if c == "#":
                right = len(platform) - idx - 2

        new_platform.append(new_row)

    return new_platform


platforms = {}
for i in range(1, 1000000000):
    for _ in range(4):
        platform = tilt(list(zip(*platform[::-1])))

    p = tuple(tuple(r) for r in platform)

    if p not in platforms:
        platforms[p] = i

    # Check to see if this repeating platform falls on the 1000000000'th cycle.
    elif (1000000000 - i) % (platforms[p] - i) == 0:
        print(
            sum(
                row.count("O") * (len(platform) - idx)
                for idx, row in enumerate(platform)
            )
        )
        break
