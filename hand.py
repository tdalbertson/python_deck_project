from deck import Deck

class Hand():
    def __init__(self):
        self.cards = []
    
    def addCard(self, card):
        self.cards.append(card)

    def showHand(self):
        print("Current hand:",self.__str__())

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

    def __len__(self):
        return len(self.cards)