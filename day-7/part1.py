"""
Advent-of-Code 2023: Day 7 / Part 1
"""

from collections import Counter

HAND_TYPES = {
    "FIVE_OF_A_KIND": 6,
    "FOUR_OF_A_KIND": 5,
    "FULL_HOUSE": 4,
    "THREE_OF_A_KIND": 3,
    "TWO_PAIR": 2,
    "ONE_PAIR": 1,
    "HIGH_CARD": 0,
}

CARD_TYPES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = "HIGH_CARD"

        cards = Counter(self.hand)

        if 5 in cards.values():
            self.type = "FIVE_OF_A_KIND"
        elif 4 in cards.values():
            self.type = "FOUR_OF_A_KIND"
        elif 3 in cards.values() and 2 in cards.values():
            self.type = "FULL_HOUSE"
        elif 3 in cards.values():
            self.type = "THREE_OF_A_KIND"
        elif list(cards.values()).count(2) == 2:
            self.type = "TWO_PAIR"
        elif 2 in cards.values():
            self.type = "ONE_PAIR"

    def __lt__(self, other):
        if HAND_TYPES[self.type] == HAND_TYPES[other.type]:
            for self_card, other_card in zip(self.hand, other.hand):
                if self_card != other_card:
                    return CARD_TYPES[self_card] < CARD_TYPES[other_card]
        return HAND_TYPES[self.type] < HAND_TYPES[other.type]

    def __str__(self):
        return self.hand


hands = []

with open("input", "r", encoding="UTF8") as file:
    for line in file:
        hands.append(Hand(*line.strip().split()))

print(sum((rank + 1) * hand.bid for rank, hand in enumerate(sorted(hands))))
