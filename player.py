from hand import Hand

class Player():
    def __init__(self, hand):
        self.playerHand = hand
        self.playerBusted = False
        self.playerStand = False

    def drawCard(self, deck, numOfCards):
        for _ in range(numOfCards):
            self.playerHand.addCard(deck.deck.pop())

    def getHandValue(self, hand):
        handValue = sum(card.value for card in self.playerHand.cards)

        return handValue