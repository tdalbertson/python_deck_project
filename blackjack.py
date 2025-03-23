from deck import Deck
from hand import Hand
from player import Player
from dealer import Dealer
import os

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
        while not self.newPlayer.playerStand:
            self.newPlayer.playerHand.showHand()
            self.checkHandValue(self.newPlayer)

            # Check for valid input
            while True:
                try:
                    choice = int(input("Hit (1) or Stand (2) or Show Card Value (3) "))
                    if choice == 1 or choice == 2:
                        break
                    elif choice == 3:
                        print(self.newPlayer.getHandValue(self.newPlayer.playerHand))
                    else:
                        raise ValueError()
                except ValueError:
                    os.system('clear')
                    print("Invalid input. Please enter either a 1 or 2")
            
            match choice:
                case 1:
                    self.newPlayer.drawCard(self.newDeck, 1)
                case 2:
                    print("You chose to stand.")
                    self.newPlayer.playerStand = True


    def checkHandValue(self, player):
        handValue = player.getHandValue(player.playerHand)
        
        if handValue == 21:
            print("Blackjack!")
        elif handValue >= 22:
            print("You busted :/")
            player.playerBusted = True