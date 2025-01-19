from deck import Deck

def main():
    newDeck = Deck()
    newDeck.showDeck()
    newDeck.shuffleDeck()
    print('\n')
    newDeck.showDeck()
    
main()