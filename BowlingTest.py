class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_i = 0
        for index in range(10):
            if self.strike(roll_i):
                result += self.strikeScore(roll_i)
                roll_i +=1
            elif self.spare(roll_i):
                result += self.spareScore(roll_i)
                roll_i +=2
            else:
                result += self.frameScore(roll_i)
            roll_i += 2
        return result

    def strike(self, roll_i):
        return self.rolls[roll_i + 1] == 10

    def spare(self, roll_i):
        return (self.rolls[roll_i] + self.rolls[roll_i + 1] == 10)

    def spareScore(self, roll_i):
        return 10 + self.rolls[roll_i + 2]

    def strikeScore(self, roll_i):
        return 10 + self.rolls[roll_i + 1] + self.rolls[roll_i + 2]

    def frameScore(self, roll_i):
        return self.rolls[roll_i] + self.rolls[roll_i + 1]
