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


class poker():

    def __init__(self, hand):
        self.hand = hand
        self.rep = {'J':'11', 'Q':'12', 'K':'13', 'A':'14'}

    def _convertToRank(self):
        converted = []
        repl = dict((re.escape(k), v) for k,v in self.rep.items())
        pattern = re.compile('|'.join(repl.keys())) 
        for i in [i[:-1] for i in self.hand]:
            x = pattern.sub(lambda m: repl[re.escape(m.group(0))], i)
            converted.append(x)
        return converted

    # def _convertToCard(self, rank):
    #     dct = {
    #         14:'A',13:'K',12:'Q',11:'J', 
    #         10:'10',9:'9',8:'8',7:'7',
    #         6:'6',5:'5',4:'4',3:'3',2:'2'
    #         }
    #     converted = list(map(dct.get, rank))
    #     return converted

    def _getRanks(self):
        ranks = list(map(int, self._convertToRank()))
        res = {i:ranks.count(i) for i in ranks}

        return ranks, res

    def isStraight(self):
        straight = False
        ranks = self._getRanks()[0]
        for comb in itertools.combinations(ranks, 5):
            if max(comb) - min(comb) == len(comb)-1:
                if len(comb) == len(set(comb)):
                    straight = True
                    ranks = sorted(ranks, reverse=True)
        return straight, ranks

    def isFlush(self):
        flush, suits = False, set()
        suits.update([i[-1] for i in self.hand])
        if len(suits) == 1: flush = True
        ranks = sorted(self._getRanks()[0], reverse=True)

        return flush, ranks

    def isStraightFlush(self):
        straightflush = False
        if self.isFlush()[0] == True and self.isStraight()[0] == True:
            straightflush = True
            
        ranks = sorted(self._getRanks()[0], reverse=True)
        return straightflush, ranks

    def isFourOfKind(self):
        fourkind = False
        res = self._getRanks()[1]

        for k, v in res.items():
            if v == 4:
                fourkind = True
                res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

        ranks_to_return = list(res.keys())
        return fourkind, ranks_to_return

    def isFullHouse(self):
        fullhouse = False
        pair, trips = self.isPair()[0], self.isTrips()[0]

        if pair == True and trips == True:
            fullhouse = True

        ranks = list(map(int, self._convertToRank()))
        res = {i:ranks.count(i) for i in ranks}
        res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        ranks_to_return = list(res.keys())

        return fullhouse, ranks_to_return


    def isTrips(self):
        trips = False
        res = self._getRanks()[1]
 
        for k, v in res.items():
            if v == 3:
                trips = True

        res = [v[0] for v in sorted(res.items(), key=lambda kv: (-kv[1], kv[0]))]
        ranks_to_return = [res[0]] + sorted(res[1:], reverse=True)

        return trips, ranks_to_return


    def isPair(self):
        twos, pair, twopair = 0, False, False
        ranks = list(map(int, self._convertToRank()))
        res = {i:ranks.count(i) for i in ranks}

        for k, v in res.items():
            if v == 2:
                twos += 1
        if twos == 1:
            pair = True
        elif twos == 2:
            twopair = True
            pair = False
        res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        ranks_to_return = list(res.keys())
        return pair, twopair, ranks_to_return


    def run(self):
    
        if self.isStraightFlush()[0] == True:
            msg, rank, val = 'Straight Flush', self.isStraightFlush()[1], 9
        elif self.isFourOfKind()[0] == True:
            msg, rank, val =  'Four of a Kind', self.isFourOfKind()[1], 8
        elif self.isFullHouse()[0] == True:
            msg, rank, val =  'Full House', self.isFullHouse()[1], 7
        elif self.isFlush()[0] == True:
            msg, rank, val =  'Flush', self.isFlush()[1], 6
        elif self.isStraight()[0] == True:
            msg, rank, val =  'Straight', self.isStraight()[1], 5
        elif self.isTrips()[0] == True:
            msg, rank, val =  'Three of a Kind', self.isTrips()[1], 4
        elif self.isPair()[1] == True:
            msg, rank, val =  'Two Pair', self.isPair()[2], 3
        elif self.isPair()[0] == True:
            msg, rank, val =  'Pair', self.isPair()[2], 2
        else:
            rank = self._getRanks()[0]
            msg, rank, val =  'Nothing', sorted(rank, reverse=True), 1


        return msg, rank, val


def hand(hole_cards, community_cards):
    best_hand, rank_list, value = '', [], 0
    all_cards = hole_cards + community_cards
    dct = {
            14:'A',13:'K',12:'Q',11:'J', 
            10:'10',9:'9',8:'8',7:'7',
            6:'6',5:'5',4:'4',3:'3',2:'2'
            }

    for comb in itertools.combinations(all_cards, 5):
        game = poker(comb)
        round = game.run()
        if round[2] > value:
            best_hand, rank_list, value = round[0], round[1], round[2]
        # handle flush order
        elif round[2] == value and sum(round[1]) > sum(rank_list):
            rank_list = round[1] 
    
    rank_list = list(map(dct.get, rank_list))

    return (best_hand, rank_list)


# tests
hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]) # ("nothing", ["A", "K", "Q", "J", "9"])
# hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]) #("pair", ["Q", "K", "J", "9"])
# hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]) #("two pair", ["K", "J", "9"])
# hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]) #("three-of-a-kind", ["Q", "J", "9"])
# hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]) #("straight", ["K", "Q", "J", "10", "9"])
# hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]) #("flush", ["Q", "J", "10", "5", "3"])
# hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]) #("full house", ["A", "K"])
# hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]) #("four-of-a-kind", ["2", "3"]),
# hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]) #("straight-flush", ["J", "10", "9", "8", "7"]),


