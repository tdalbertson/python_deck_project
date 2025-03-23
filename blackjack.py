from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer

class BlackJack():
    def __init__(self):
        self.newDeck = Deck()
        self.newPlayer = Player(Hand())
        self.newDealer = Dealer()

    def start(self):
        print("New game of Blackjack\n")
        self.newDeck.shuffleDeck()
        self.newPlayer.drawCard(self.newDeck, 2)
        self.newDealer.drawCard(self.newDeck, 2)

        # Start Player's turn
        self.checkHandValue(self.newPlayer.playerHand)

        print(str(self.newPlayer.playerHand))
        print(self.newDealer.playerHand)

    def checkHandValue(self, player):
        handValue = 0
        for card in player.hand:
            print(card)  
            # handValue += card.value
        
        # if handValue == 21:
        #     print("Blackjack!")
        # elif handValue >= 22:
        #     print("You busted :/")