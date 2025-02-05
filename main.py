from deck import Deck
from hand import Hand

def main():
    
    newDeck = Deck()
    newDeck.shuffleDeck()

    newHand = Hand()

    newHand.buildHand("BlackJack", newDeck)
    
    print(str(newHand))

main()