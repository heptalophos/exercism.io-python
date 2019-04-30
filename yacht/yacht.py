from collections import Counter

def counts(n):
    return lambda dice: n * Counter(dice)[n]

def str8(dice):
    lgth = 1
    while min(dice) + lgth in dice:
        lgth += 1
    return lgth
    
YACHT = lambda dice: 50 if len(dice) == 5 and len(set(dice)) == 1 else 0
ONES = counts(1)
TWOS = counts(2)
THREES = counts(3)
FOURS = counts(4)
FIVES = counts(5)
SIXES = counts(6)
FULL_HOUSE = lambda dice : sum(dice) if sorted(tuple(Counter(dice).values())) == [2, 3] else 0
FOUR_OF_A_KIND = lambda dice : [(4*key if val >= 4 else 0) for key, val in Counter(dice).items()][0]
LITTLE_STRAIGHT = lambda dice : 30 if str8(dice) == 5 and max(dice) == 5 else 0
BIG_STRAIGHT = lambda dice : 30 if str8(dice) == 5 and max(dice) == 6 else 0
CHOICE = lambda dice : sum(dice) 


def score(dice, category):
    return category(dice)
