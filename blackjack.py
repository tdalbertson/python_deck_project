from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer

class BlackJack():
    def __init__(self):
        self.newDeck = Deck().generateDeck()
        self.newPlayer = Player(Hand())
        self.newDealer = Dealer()

    def start(self):
        print("New game of Blackjack\n")
        self.newPlayer.drawCard(self.newDeck, 2)
        self.newDealer.drawCard(self.newDeck, 2)

        print(str(self.newPlayer.playerHand))
        print(self.newDealer.playerHand)
