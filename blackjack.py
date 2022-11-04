import random

"""
GLOBAL VARIABLES USED BY ALL CLASSES
"""
suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


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

    def __str__(
            self):  # Allows user to see the composition of the deck by calling the print function of the Deck object
        deck_composition = ""
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The deck has: " + deck_composition

    def shuffle(self):  # Shuffles the list
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:  # Allows user to see what cards they possess

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)  # The card passed in is the card object obtained from the Deck().deal method
        self.value += values[card.rank]  # Obtains the value of card object and adds it to the self.value attribute

        if card.rank == 'Ace':  # Tracking aces
            self.aces += 1

    def adjust_for_aces(self):  # Method that adjusts for aces incase the value of the players hand exceeds 21.
        # To compensate the values of the aces is reduced from 11 to 1.
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips: # Chips class that keeps track of players starting chips, bets and winnings.

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
