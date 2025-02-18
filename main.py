from deck import Deck
from hand import Hand
from player import Player

def main():
    
    newPlayer = Player()
    newDeck = Deck()
    newDeck.shuffleDeck()

    newHand = Hand()
    print(len(newHand))
    print(newDeck.length)

main()