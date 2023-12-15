"""
Advent-of-Code 2023: Day 10 / Part 1
"""
import operator
import sys
from collections import defaultdict

tiles = defaultdict(lambda: ".")

start = None
with open("test-input", "r", encoding="UTF8") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            tiles[(x, y)] = c
            if c == "S":
                start = (x, y)

MOVES = {
    (0, -1): {"next": "|7F", "not_from": "-7F"},
    (1, 0): {"next": "-7J", "not_from": "|7J"},
    (0, 1): {"next": "|JL", "not_from": "-JL"},
    (-1, 0): {"next": "-LF", "not_from": "|LF"},
}


pos = start
previous = None
steps = 0
while True:
    finish = False
    for delta, move in MOVES.items():
        step = tuple(map(operator.add, pos, delta))

        # Don't move back.
        if step == previous:
            continue

        # Move forward but only if it's allowed from the current position.
        if tiles[step] in move["next"] and tiles[pos] not in move["not_from"]:
            finish = False
            previous, pos, steps = pos, step, steps + 1
            break

        # Could be the potential finish, if no more moves are applied.
        if tiles[step] == "S":
            finish = True

    if finish:
        print((steps + 1) // 2)
        break
