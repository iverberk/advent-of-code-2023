"""
Advent-of-Code 2023: Day 7 / Part 2
"""

from collections import Counter
from itertools import product

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
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}

CARD_TYPES_WITHOUT_JOKER = {
    card: rank for card, rank in CARD_TYPES.items() if card != "J"
}

JOKER_COMBINATIONS = {
    1: list(product(CARD_TYPES_WITHOUT_JOKER, repeat=1)),
    2: list(product(CARD_TYPES_WITHOUT_JOKER, repeat=2)),
    3: list(product(CARD_TYPES_WITHOUT_JOKER, repeat=3)),
    4: list(product(CARD_TYPES_WITHOUT_JOKER, repeat=4)),
    5: list(product(CARD_TYPES_WITHOUT_JOKER, repeat=5)),
}


class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        self.type = "HIGH_CARD"

        if "J" not in hand:
            self.type = self.find_hand_type(self.hand)
        else:
            jokers = [idx for idx, card in enumerate(self.hand) if card == "J"]
            max_hand_type = "HIGH_CARD"

            # Iterate over all the joker combinations.
            for combination in JOKER_COMBINATIONS[len(jokers)]:
                # Replace hand with current joker combination.
                hand = list(self.hand)
                for idx, joker in enumerate(jokers):
                    hand[joker] = combination[idx]
                hand = "".join(hand)

                hand_type = self.find_hand_type(hand)
                if HAND_TYPES[hand_type] > HAND_TYPES[max_hand_type]:
                    max_hand_type = hand_type

            self.type = max_hand_type

    def find_hand_type(self, hand):
        card_type = "HIGH_CARD"

        cards = Counter(hand)

        if 5 in cards.values():
            card_type = "FIVE_OF_A_KIND"
        elif 4 in cards.values():
            card_type = "FOUR_OF_A_KIND"
        elif 3 in cards.values() and 2 in cards.values():
            card_type = "FULL_HOUSE"
        elif 3 in cards.values():
            card_type = "THREE_OF_A_KIND"
        elif list(cards.values()).count(2) == 2:
            card_type = "TWO_PAIR"
        elif 2 in cards.values():
            card_type = "ONE_PAIR"

        return card_type

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
