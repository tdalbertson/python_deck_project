from hand import Hand

class Player():
    def __init__(self, hand):
        self.playerHand = hand

    def drawCard(self, deck, numOfCards):
        for _ in range(numOfCards):
            self.playerHand.addCard(deck.deck.pop())
