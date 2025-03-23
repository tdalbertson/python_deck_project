class Card:
    def __init__(self, suit, card_type, value):
        self.suit = suit
        self.value = value
        self.card_type = card_type

    def __str__(self):
        return f"{self.card_type} of {self.suit}"