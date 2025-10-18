from collections import Counter

NUMBERS = {"2","3","4","5","6","7","8","9","10"}
FACES   = {"J","Q","K"}

def all_red(hand):       return all(c.color == "red" for c in hand)
def all_black(hand):     return all(c.color == "black" for c in hand)
def all_hearts(hand):    return all(c.suit  == "hearts" for c in hand)
def all_queens(hand):    return all(c.rank  == "Q" for c in hand)
def all_numbers(hand):   return all(c.rank in NUMBERS for c in hand)
def all_faces(hand):     return all(c.rank in FACES   for c in hand)
def same_color(hand):    return len({c.color for c in hand}) == 1
def same_suit(hand):     return len({c.suit  for c in hand}) == 1

# “3-of” patterns are much more frequent → better for K-2:
def at_least_three_red(hand):     return sum(c.color == "red"     for c in hand)   >= 3
def at_least_three_black(hand):   return sum(c.color == "black"   for c in hand)   >= 3
def at_least_three_hearts(hand):  return sum(c.suit  == "hearts"  for c in hand)   >= 3
def at_least_three_numbers(hand): return sum(c.rank  in NUMBERS   for c in hand)   >= 3
def at_least_three_faces(hand):   return sum(c.rank  in FACES     for c in hand)   >= 3

PATTERNS = {
    # your originals
    "All Red": all_red,
    "All Black": all_black,
    "All Hearts": all_hearts,
    "All Queens": all_queens,

    # simple, common wins
    "All Numbers": all_numbers,
    "All Face Cards": all_faces,
    "Same Color": same_color,
    "Same Suit": same_suit,

    # kid-friendly frequent patterns (3-of)
    "3+ Red": at_least_three_red,
    "3+ Black": at_least_three_black,
    "3+ Hearts": at_least_three_hearts,
    "3+ Numbers": at_least_three_numbers,
    "3+ Face Cards": at_least_three_faces,
}
