import random

"""
GLOBAL VARIABLES USED BY ALL CLASSES
"""
suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10}


class Card:  # Card class

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:  # Deck class that automatically generates a deck by creating a list of card objects

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):  # Allows user to see the composition of the deck by calling the print function of the Deck object
        deck_composition = ""
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The deck has: " + deck_composition

    def shuffle(self):  # Shuffles the list
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
