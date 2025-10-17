class K2_pattern:

    def evaluate(self, cards):
        if self.all_red(cards):
            return True
        if self.all_black(cards):
            return True
        if self.all_spade(cards):
            return True
        if self.all_queen(cards):
            return True
        if self.all_5(cards):
            return True
        if self.all_diamonds(cards):
            return True
        return False

    def all_red(self, cards):
        return all(c.is_red() for c in cards)

    def all_black(self, cards):
        return all(c.is_black() for c in cards)

    def all_spade(self, cards):
        return all(c.suit.lower() == 'spades' for c in cards)

    def all_queen(self, cards):
        return all(c.card_no.lower() == 'queen' for c in cards)

    def all_5(self, cards):
        return all(c.card_no.lower() == '5' for c in cards)

    def all_diamonds(self, cards):
        return all(c.suit.lower() == 'diamonds' for c in cards)

