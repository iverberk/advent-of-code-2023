"""
Advent-of-Code 2023: Day 1 / Part 2
"""

SUM = 0

NUMBERS = [
    (3, "one", "1"),
    (3, "two", "2"),
    (5, "three", "3"),
    (4, "four", "4"),
    (4, "five", "5"),
    (3, "six", "6"),
    (5, "seven", "7"),
    (5, "eight", "8"),
    (4, "nine", "9"),
]

with open("input", "r", encoding="UTF8") as file:
    for line in file:
        FIRST, LAST = "", ""
        i = 0
        while i < len(line):
            if line[i].isdigit():
                if not FIRST:
                    FIRST = line[i]
                LAST = line[i]

            for number in NUMBERS:
                if i + number[0] < len(line) and line[i : i + number[0]] == number[1]:
                    if not FIRST:
                        FIRST = number[2]
                    LAST = number[2]
                    break

            i += 1

        SUM += int(FIRST + LAST)

    print(SUM)
