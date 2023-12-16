"""
Advent-of-Code 2023: Day 16 / Part 1
"""

c = []

with open("input", "r", encoding="UTF8") as file:
    for row in file:
        c.append(list(row.strip()))

stack = [(0, 0, 1, 0)]
seen = set()
energized = set()

while stack:
    x, y, dx, dy = stack.pop()

    while 0 <= x < len(c[0]) and 0 <= y < len(c):
        if (x, y, dx, dy) in seen:
            break

        seen.add((x, y, dx, dy))
        energized.add((x, y))

        match c[y][x]:
            case ".":
                x += dx
                y += dy

            case "-":
                if dx:
                    x += dx
                    continue

                stack.append((x - 1, y, -1, 0))
                stack.append((x + 1, y, 1, 0))
                break

            case "|":
                if dy:
                    y += dy
                    continue

                stack.append((x, y - 1, 0, -1))
                stack.append((x, y + 1, 0, 1))
                break

            case "/":
                if dy == 1:
                    dx, dy = -1, 0
                    x += dx
                elif dy == -1:
                    dx, dy = 1, 0
                    x += dx
                elif dx == 1:
                    dx, dy = 0, -1
                    y += dy
                elif dx == -1:
                    dx, dy = 0, 1
                    y += dy

            case "\\":
                if dy == 1:
                    dx, dy = 1, 0
                    x += dx
                elif dy == -1:
                    dx, dy = -1, 0
                    x += dx
                elif dx == 1:
                    dx, dy = 0, 1
                    y += dy
                elif dx == -1:
                    dx, dy = 0, -1
                    y += dy

print(len(energized))
