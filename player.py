import random

class Player:
    def __init__(self):
        self.pos = 0
        self.balance = 15000
        self.properties = [0,0,0,0,0,0,0,0,0,0]

    def roll(self):
        first =  random.randint(1,6)
        second = random.randint(1,6)
        return first+second

    def decide():
        pass

