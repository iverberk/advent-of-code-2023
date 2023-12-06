"""
Advent-of-Code 2023: Day 5 / Part 2
"""

almanac = []
seeds = []

with open("test-input", "r", encoding="UTF8") as file:
    in_map = False
    conversion_map = []
    for line in file:
        line = line.strip()

        if "seeds" in line:
            seeds = [int(s) for s in line.split(":")[1].split()]
            continue

        if "map:" in line and not in_map:
            in_map = True
            conversion_map = []
            continue

        if not line and in_map:
            in_map = False
            almanac.append(conversion_map)
            continue

        if in_map:
            conversion_map.append([int(x) for x in line.split()])
