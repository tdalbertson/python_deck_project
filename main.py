from blackjack import BlackJack
import sys

# Python version check (3.10 or higher)
required_version = (3, 10)
if sys.version_info < required_version:
    print(f"Error: Please use Python {required_version[0]}.{required_version[1]} or later.")
    sys.exit(1)

def main():
    newGame: BlackJack = BlackJack()
    newGame.start()    

main()