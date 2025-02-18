from deck import Deck

class Player():
    def __init__(self, hand):
        self.playerHand = hand

    def drawCard(self, deck, numOfCards):
        for card in range(0, numOfCards + 1):
            self.playerHand.append(deck.pop())
