import operator
from itertools import combinations

galaxies, galaxies_x, galaxies_y = set(), set(), set()
MAX_X, MAX_Y = 140, 140

with open("input", "r", encoding="UTF8") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line.strip()):
            if c == "#":
                galaxies.add((x, y))
                galaxies_x.add(x)
                galaxies_y.add(y)

dx = 0
for x in range(0, MAX_X):
    if x not in galaxies_x:
        galaxies = {
            tuple(map(operator.add, galaxy, (1, 0))) if galaxy[0] > x + dx else galaxy
            for galaxy in galaxies
        }
        dx += 1


dy = 0
for y in range(0, MAX_Y):
    if y not in galaxies_y:
        galaxies = {
            tuple(map(operator.add, galaxy, (0, 1))) if galaxy[1] > y + dy else galaxy
            for galaxy in galaxies
        }
        dy += 1

print(
    sum(
        abs((pair[0][0] - pair[1][0])) + abs((pair[0][1] - pair[1][1]))
        for pair in combinations(galaxies, 2)
    )
)
