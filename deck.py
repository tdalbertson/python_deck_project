from random import shuffle

class Deck:
    cards = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King"
    }
    
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    
    def __init__(self):
        self.deck = self.generateDeck()
        
    def generateDeck(self):
        full_deck = []
        for suit in self.suits:
            for card in self.cards.values():
                full_deck.append(f"{card} of {suit}")
        return full_deck

    def shuffleDeck(self):
        return shuffle(self.deck)

    def showDeck(self):
        for card in self.deck:
            print(card)