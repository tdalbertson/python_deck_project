from deck import Deck

def main():
    
    newDeck = Deck()
    print(str(newDeck))

    newDeck.shuffleDeck()
    print(str(newDeck))

    newDeck.sortDeck()
    print(str(newDeck))
    

main()