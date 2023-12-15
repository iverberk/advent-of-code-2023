"""
Advent-of-Code 2023: Day 13 / Part 1
"""

# pylint: disable=C0103

patterns = []
with open("input", "r", encoding="UTF8") as file:
    pattern = []
    for line in file:
        line = line.strip()
        if not line:
            patterns.append(pattern)
            pattern = []
            continue

        pattern.append(line)


notes_sum = 0
for pattern in patterns:
    # Sweep for vertical reflection lines
    for x in range(len(pattern[0]) - 1):
        candidate = True
        for y, _ in enumerate(pattern):
            # Check for non-symmetry
            if pattern[y][x] != pattern[y][x + 1]:
                candidate = False
                break

        # Potential vertical reflication line, check full symmetry.
        if candidate:
            left, right = x - 1, x + 2
            found = True
            while left >= 0 and right < len(pattern[0]):
                symmetrical = True
                for y, _ in enumerate(pattern):
                    # Check for non-symmetry
                    if pattern[y][left] != pattern[y][right]:
                        symmetrical = False
                        break

                if not symmetrical:
                    found = False
                    break

                left, right = left - 1, right + 1

            if found:
                notes_sum += x + 1
                break

    # Sweep for horizontal reflection lines
    for y in range(len(pattern) - 1):
        candidate = True
        for x, _ in enumerate(pattern[y]):
            # Check for non-symmetry
            if pattern[y][x] != pattern[y + 1][x]:
                candidate = False
                break

        if candidate:
            up, down = y - 1, y + 2
            found = True
            while up >= 0 and down < len(pattern):
                symmetrical = True
                for x, _ in enumerate(pattern[0]):
                    # Check for non-symmetry
                    if pattern[up][x] != pattern[down][x]:
                        symmetrical = False
                        break

                if not symmetrical:
                    found = False
                    break

                up, down = up - 1, down + 1

            if found:
                notes_sum += (y + 1) * 100

print(notes_sum)
