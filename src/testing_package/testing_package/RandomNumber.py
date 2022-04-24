from random import randint as r


class RandomNumber:
    def __init__(self, high, low):
        self.max = high
        self.min = low

    def create(self):
        num = r(self.max, self.min)
        print(num)
