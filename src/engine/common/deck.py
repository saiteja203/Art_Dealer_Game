import random
SUITS = ["hearts","diamonds","clubs","spades"]
RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
COLORS = {"hearts":"red","diamonds":"red","clubs":"black","spades":"black"}

class Card:
    def __init__(self, suit, rank):
        self.suit, self.rank = suit, rank
        self.color = COLORS[suit]
    def __repr__(self): return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self._cards = [Card(s, r) for s in SUITS for r in RANKS]
        random.shuffle(self._cards)
    def draw(self, n=4):
        hand, self._cards = self._cards[:n], self._cards[n:]
        return hand
    def reset(self):
        self.__init__()
