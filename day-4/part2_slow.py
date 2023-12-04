"""
Advent-of-Code 2023: Day 4 / Part 2
"""

import re

cards = {}

with open("input", "r", encoding="UTF8") as file:
    for line in file:
        m = re.search(r".* (\d+):(.*)\|(.*)", line.strip())
        g = int(m.group(1))
        w = {int(x) for x in m.group(2).split()}
        n = {int(x) for x in m.group(3).split()}

        cards[g] = {"winning": len(w & n), "amount": 1}

MAX_CARDS = max(cards.keys()) + 1

# Loop over the cards in ascending order.
for card in range(1, MAX_CARDS):
    if cards[card]["winning"]:
        # Iterate over all the instances of this card.
        for _ in range(0, cards[card]["amount"]):
            # Create additional card instances based on the winning amount.
            for instance in range(
                card + 1, min(card + 1 + cards[card]["winning"], MAX_CARDS)
            ):
                cards[instance]["amount"] += 1

print(sum(card["amount"] for card in cards.values()))
