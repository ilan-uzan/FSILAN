# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self):
        self.cards = []
        self.create_deck()
    
    def create_deck(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
    
    def shuffle(self):
        if len(self.cards) != 52:
            self.create_deck()
        random.shuffle(self.cards)
    
    def deal(self):
        if not self.cards:
            return None 
        return self.cards.pop()


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    
    print("Dealing 5 cards:")
    for i in range(5):
        card = deck.deal()
        print(f"Card {i+1}: {card}")
    
    print(f"\nRemaining cards in deck: {len(deck.cards)}")