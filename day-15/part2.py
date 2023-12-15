"""
Advent-of-Code 2023: Day 15 / Part 2
"""

from collections import deque

sequence = open("input").readline().strip().split(",")
boxes = [deque() for _ in range(256)]
lengths = {}


def HASH(inp):
    current_value = 0
    for c in inp:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    return current_value


for step in sequence:
    if "-" in step:
        label = step[:-1]
        h = HASH(label)
        if label in boxes[h]:
            boxes[h].remove(label)

    if "=" in step:
        label, length = step.split("=")
        lengths[label] = int(length)

        h = HASH(label)
        if label in boxes[h]:
            n = boxes[h].index(label)

            boxes[h].rotate(-n)
            boxes[h].popleft()
            boxes[h].appendleft(label)
            boxes[h].rotate(n)
        else:
            boxes[h].append(label)

total_power = 0
for box_nr, box in enumerate(boxes):
    for slot, label in enumerate(box):
        total_power += (box_nr + 1) * (slot + 1) * lengths[label]

print(total_power)
