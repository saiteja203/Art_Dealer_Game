from engine.common.Card import card
import random


class Deck:
    SUITS = ["Hearts", "Spades", "Diamonds", "Clubs"]
    CARD_NOS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Joker', 'Queen', 'King']

    def __init__(self):
        # creating deck of cards
        self.cards = [card(s, c) for s in self.SUITS for c in self.CARD_NOS]
        # to shuffle the deck of cards
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def card_drawn(self, n):
        if n < 1:
            return []
        drawn = []
        for _ in range(n):
            drawn.append(self.cards.pop())
        return drawn if n>1 else drawn[0]

    def reset(self):
        self.__init__()
        print("reset successful")

    def remaining_cards_in_deck(self):
        return len(self.cards)


