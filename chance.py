class Chance:
    def __init__(self,payment,travel_pos):
        self.payment = payment
        self.travel_pos = travel_pos


class ChanceStack:
    def __init__(self):
        self.chance_stack = []