import random

class DataGen:
    def __init__(self, items: list):
        self.items = items

    def generate(self):
        return random.choice(self.items) if self.items else None