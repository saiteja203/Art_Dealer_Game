class card:
    def __init__(self, suit, card_no):
        self.suit = suit
        self.card_no = card_no
    def __repr__(self):
         return f"{self.card_no} of {self.suit}"
    def is_red(self):
        if self.suit in ("Hearts", "Diamonds"):
            return True
    def is_black(self):
        if self.suit in ("Clubs", "Spades"):
            return True

