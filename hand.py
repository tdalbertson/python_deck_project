from deck import Deck

class Hand(Deck):
    def __init__(self):
        self.deck = []
        self.shuffled = False
        self.sorted = False

    def buildHand(self, gameType, currentDeck):
        if gameType == "BlackJack":
            self.drawCard(currentDeck, 2)
    
    def drawCard(self, currentDeck: Deck, numOfCards: int):
        for card in range(0, numOfCards):
            self.deck.append(currentDeck.deck.pop(0))
            self.length = len(self.deck)

    