def all_red(hand):    return all(c.color == "red" for c in hand)
def all_black(hand):  return all(c.color == "black" for c in hand)
def all_hearts(hand): return all(c.suit == "hearts" for c in hand)
def all_queens(hand): return all(c.rank == "Q" for c in hand)

PATTERNS = {
    "All Red": all_red,
    "All Black": all_black,
    "All Hearts": all_hearts,
    "All Queens": all_queens,
}
