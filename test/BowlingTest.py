from unittest import TestCase

from bowling import Game


class BowlingTest(TestCase):

    def setUp(self):
        self.game = Game.Game()

    def test_GutterGame(self):
        self.rollx(1, 20)
        assert self.game.score() == 0

    def test_aSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollx(0, 17)
        assert self.game.score() == 16

    def test_aStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollx(0, 17)
        assert self.game.score() == 24

    def test_perfectgame(self):
        self.rollx(10, 12)
        assert self.game.score() == 300

    def rollx(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
