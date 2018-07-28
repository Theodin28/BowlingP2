import unittest
import BowlingTest

class testBowlingGame(unittest.TestCase):


    def setup(self):
        self.game = BowlingTest.BowlingGame()


    def testGutterGame(self):
        self.rollx(1, 20)
        assert self.game.score() == 0

    def testaSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollx(0, 17)
        assert self.game.score() == 16

    def testaStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollx(0, 17)
        assert self.score() == 24

    def perfectgame(self):
        self.rollx(10, 12)
        assert self.game.score() == 300

    def rollx(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)