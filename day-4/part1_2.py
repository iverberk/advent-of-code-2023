"""
Advent-of-Code 2023: Day 4 / Part 1 and 2
"""

import re
from collections import defaultdict

POINTS = 0

cards = defaultdict(int)

with open("input", "r", encoding="UTF8") as file:
    for line in file:
        m = re.search(r".* (\d+):(.*)\|(.*)", line.strip())
        card = int(m.group(1))
        w = {int(x) for x in m.group(2).split()}
        n = {int(x) for x in m.group(3).split()}

        cards[card] += 1
        l = len(w & n)
        if l:
            POINTS += 2 ** (l - 1)

            for i in range(1, l + 1):
                cards[card + i] += cards[card]

print(POINTS, sum(cards.values()))
