'''
Possible hands are, in descending order of value:

Straight-flush (five consecutive ranks of the same suit). Higher rank is better.

Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.

Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards, then rank of the pair.

Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.

Straight (five consecutive ranks). Higher rank is better.

Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards, 
then the highest other rank, then the second highest other rank.

Two pair (two cards of the same rank, two cards of another rank). 
Tiebreaker is first the rank of the high pair, then the rank of the low pair and then the rank of the remaining card.

Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.

Nothing. Tiebreaker is the rank of the cards from high to low.


Given hole cards and community cards, complete the function 'hand' to return the type of hand 
and the list of ranks used in decreasing order of significance.

hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
# ...should return ("pair", ranks: ["A", "J", "10", "5"]})
hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
# ...should return ("flush", ["Q", "J", "10", "5", "3"])

EDIT: for Straights with an Ace, only the ace-high straight is accepted. 
An ace-low straight is invalid (ie. A,2,3,4,5 is invalid). This is consistent with the author's reference solution. 
'''
import re
import itertools


(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"])

class poker:
    def __init__(self, hole_cards, community_cards):
        self.hand = hole_cards + community_cards
        self.rep = {'J':'11', 'Q':'12', 'K':'13', 'A':'14'}

hand = ["Q♠", "2♦", "J♣", "10♥", "9♥", "K♥", "3♦"]
rep = {'J':'11', 'Q':'12', 'K':'13', 'A':'14'}

def convertToRank(hand, rep):
    renamed = []
    rep = dict((re.escape(k), v) for k,v in rep.items())
    pattern = re.compile('|'.join(rep.keys()))
    for i in [i[:-1] for i in hand]:
        x = pattern.sub(lambda m: rep[re.escape(m.group(0))], i)
        renamed.append(x)
    return renamed

def convertToCard(rank):
    return

def isStraight(hand):
    ranks = list(map(int, convertToRank(hand, rep)))
    straights = []

    for comb in itertools.combinations(ranks, 5):
        if max(comb) - min(comb) == len(comb)-1:
            if len(comb) == len(set(comb)):
                straights.append(sorted(comb))
    # best_straight = sorted(straights)[-1]
    if len(straights) > 0: return True
    else: return False

hand = ["8♠", "7♠", "9♠", "J♠", "10♠"]

def isFlush(hand):
    flush = set()
    flush.update([i[-1] for i in hand])

    if len(flush) == 1: return True
    else: return False

def isStraightFlush(hand):
    if isFlush(hand) == True and isStraight(hand) == True:
        return True
    else:
        return False


def isFourOfKind(hand):
    fourkind = False
    ranks = list(map(int, convertToRank(hand, rep)))
    res = {i:ranks.count(i) for i in ranks}
    for k, v in res.items():
        if v == 4:
            fourkind = True
            res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

    ranks_to_return = list(res.keys())

    return fourkind, ranks_to_return


def isFullHouse(hand):
    twos, threes, fullhouse = 0, 0, False

    ranks = list(map(int, convertToRank(hand, rep)))
    res = {i:ranks.count(i) for i in ranks}
    for k, v in res.items():
        if v == 2:
            twos = k
        elif v == 3:
            threes = k
    if twos != 0 and threes != 0:
        fullhouse = True

    res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
    ranks_to_return = list(res.keys())

    # add mapping back to JQKA

    return fullhouse, ranks_to_return


def isTrips(hand):
    return

def isTwoPair(hand):
    return

def isPair(hand):
    return 

def isHighCard(hand):
    return






def hand(hole_cards, community_cards):
    best_hand = ''
    rank_list = []
    ac = hole_cards + community_cards
    # loop all combinations of 5 cards, to allow isStraightFlush logic to stand
    
    return (best_hand, rank_list)



# tests
hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]) # ("nothing", ["A", "K", "Q", "J", "9"])
hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]) #("pair", ["Q", "K", "J", "9"])
hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]) #("two pair", ["K", "J", "9"])
hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]) #("three-of-a-kind", ["Q", "J", "9"])
hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]) #("straight", ["K", "Q", "J", "10", "9"])
hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]) #("flush", ["Q", "J", "10", "5", "3"])
hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]) #("full house", ["A", "K"])
hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]) #("four-of-a-kind", ["2", "3"]),
hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]) #("straight-flush", ["J", "10", "9", "8", "7"]),


