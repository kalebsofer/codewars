import pytest
from interview_prep.kata.bowling import gene2, bowlingGame


def test_gene2():
    assert gene2(2) == 4


#  leading underscore to indicate weak 'internal use' (won't be imported with *)
def _roll_many(self, pins, num):
    for i in range(num):
        self.game.roll(pins)

def _roll_spare(self):
    self.game.roll(5)
    self.game.roll(5)


def setUp(self):
    self.game = bowlingGame()

def test_gutter_game(self):
    self._roll_many(0, 20)
    assert self.game.total_score() == 0

def test_all_ones(self):
    self._roll_many(1, 20)
    assert self.game.total_score() == 20

def test_one_spare(self):
    self._roll_spare()
    self.game.roll(3)
    self._roll_many(0, 17)
    assert self.game.total_score() == 16

def test_one_strike(self):
    self.game.roll(10)
    self.game.roll(3)
    self.game.roll(4)
    self._roll_many(0, 16)
    assert self.game.total_score() == 24

def test_perfect_game(self):
    self._roll_many(10, 12)
    assert self.game.total_score() == 300

def test_simple_game(self):
    for pins in [1, 4, 4, 5, 6, 4, 5, 5,
                 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]:
        self.game.roll(pins)
    assert self.game.total_score() == 133

# def test_simple_game_string(self):
    # return
