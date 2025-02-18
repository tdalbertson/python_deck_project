from deck import Deck

class Hand(Deck):
    def __init__(self):
        super().__init__()
        self.deck = []
    
    def drawCard(self, currentDeck: Deck, numOfCards: int, hand: list):
        for card in range(0, numOfCards):
            hand.append(currentDeck.deck.pop(0))

        return hand