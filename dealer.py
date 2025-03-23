from player import Player
from hand import Hand

class Dealer(Player):
    def __init__(self):
        super().__init__(Hand())