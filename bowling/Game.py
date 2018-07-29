class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_i = 0
        for index in range(10):
            if self.strike(roll_i):
                result += self.strike_score(roll_i)
                roll_i += 1
            elif self.spare(roll_i):
                result += self.spare_score(roll_i)
                roll_i += 2
            else:
                result += self.frame_score(roll_i)
            roll_i += 2
        return result

    def strike(self, roll_i):
        return self.rolls[roll_i + 1] == 10

    def spare(self, roll_i):
        return self.rolls[roll_i] + self.rolls[roll_i + 1] == 10

    def spare_score(self, roll_i):
        return 10 + self.rolls[roll_i + 2]

    def strike_score(self, roll_i):
        return 10 + self.rolls[roll_i + 1] + self.rolls[roll_i + 2]

    def frame_score(self, roll_i):
        return self.rolls[roll_i] + self.rolls[roll_i + 1]
