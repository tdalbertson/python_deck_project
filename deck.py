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
        self.sorted = False
        
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

    def sortDeck(self):
        for deck_range in range(self.length - 1, 0 , -1):
            for current_card in range(deck_range):
                if self.deck[current_card].value > self.deck[current_card + 1].value:
                    self.deck[current_card], self.deck[current_card + 1] = self.deck[current_card + 1], self.deck[current_card]

        self.shuffled = False
        self.sorted = True

    def showDeck(self):
        if self.shuffled:
            print("\nShuffled deck:")
        elif self.sorted:
            print("\nSorted deck:")
        for card in self.deck:
            print(f"{card.card_type} of {card.suit} with a value of {card.value}")

    def __str__(self):
        card_strings = []

        for card in self.deck:
            card_strings.append(f"{card.card_type} of {card.suit} with a value of {card.value}")

        if self.shuffled:
            return "\nShuffled:\n" + '\n'.join(card_strings)
        elif self.sorted:
            return "\nSorted:\n" + '\n'.join(card_strings)

        return '\n'.join(card_strings)