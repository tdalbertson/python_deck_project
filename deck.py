from random import randint
from card import Card

class Deck:
    _cards = {
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
    
    _suits = ("Hearts", "Clubs", "Diamonds", "Spades")
    
    def __init__(self):
        self.deck = self.generateDeck()
        self.length = len(self.deck)
        self.shuffled = False
        
    def generateDeck(self):
        full_deck = []

        for suit in self._suits:
            for card_value in self._cards.keys():
                newCard = Card(suit, self._cards[card_value], card_value)
                full_deck.append(newCard)

        return full_deck

    def shuffleDeck(self):
        shuffledDeck = []

        while len(self.deck) > 0:
            i = randint(0, len(self.deck) - 1)
            shuffledDeck.append(self.deck.pop(i))
        
        self.deck = shuffledDeck
        self.shuffled = True

    def showDeck(self):
        if(self.shuffled):
            print("\nShuffled deck:")
        for card in self.deck:
            print(f"{card.card_type} of {card.suit} with a value of {card.value}")