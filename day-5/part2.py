"""
Advent-of-Code 2023: Day 5 / Part 2
"""

from collections import deque

almanac = []
seeds = []

with open("input", "r", encoding="UTF8") as file:
    in_map = False
    conversion_map = []
    for line in file:
        line = line.strip()

        if "seeds" in line:
            seed_ranges = [int(s) for s in line.split(":")[1].split()]
            seeds = list(zip(seed_ranges[::2], seed_ranges[1::2]))
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


def apply_map(ranges, mappings):
    transformed = set()

    ranges = deque(ranges)

    while ranges:
        r = ranges.popleft()
        for m in mappings:
            r_low, r_high, r_range = r[0], r[0] + r[1] - 1, r[1]
            m_start, m_low, m_high = m[0], m[1], m[1] + m[2] - 1

            # Entire range falls exactly in the mapping.
            if r_low >= m_low and r_high <= m_high:
                transformed.add((r_low - m_low + m_start, r_range))

            # Range needs to be split because the lower range boundary falls within the mapping.
            elif m_low <= r_low <= m_high < r_high:
                ranges.append((m_high + 1, r_high - m_high))
                transformed.add((r_low - m_low + m_start, m_high - r_low + 1))

            # Range needs to be split because the higher range boundary falls within the mapping.
            elif r_low < m_low <= r_high <= m_high:
                ranges.append((r_low, m_low - r_low))
                transformed.add((m_start, r_high - m_low + 1))

    return transformed


for maps in almanac:
    seeds = apply_map(seeds, maps)

print(min(seeds)[0])
