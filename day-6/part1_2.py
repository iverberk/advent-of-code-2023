"""
Advent-of-Code 2023: Day 6 / Part 1 and 2
"""
import math

with open("input", "r", encoding="UTF8") as file:
    games = list(
        zip(
            [int(t) for t in file.readline().strip().split(":")[1].split()],
            [int(d) for d in file.readline().strip().split(":")[1].split()],
        )
    )

    def wins(time, distance):
        """
        Calculates all the winning 'hold' values for a given time and distance.
        """
        discriminant = (time**2) - (-4 * -distance)
        upper = (-time - math.sqrt(discriminant)) / -2
        lower = (-time + math.sqrt(discriminant)) / -2

        return math.ceil(upper) - math.floor(lower) - 1

    part1 = math.prod([wins(game[0], game[1]) for game in games])
    part2 = wins(
        int("".join(str(game[0]) for game in games)),
        int("".join(str(game[1]) for game in games)),
    )
    print(part1, part2)
