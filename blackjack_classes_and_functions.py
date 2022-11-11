import random

"""
GLOBAL VARIABLES USED BY ALL CLASSES
"""
suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# global playing


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

    def __str__(self):  # Allows user to see the composition of the deck by calling the print function of the Deck
        # object
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


class Chips:  # Chips class that keeps track of players starting chips, bets and winnings.

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


"""
GAME RELATED FUNCTIONS
"""


def take_bet(chips):  # Function for taking bets
    # The function also checks whether a players bet can be covered by their available chips.
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry! a bet must be an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! You have: {}'.format(chips.total))
            else:
                break


def hit(deck, hand):  # Function that enables player to take hits
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


playing = True


def hit_or_stand(deck, hand):
    global playing
    while playing:
        x = input('Hit or Stand? Enter h or s: ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealers turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter either h or s")
            continue
        break


def show_some(player, dealer):  # Function that shows only one of the dealers cards and all the players cards

    print("\n Dealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)


def show_all(player, dealer):  # Function that displays all dealer and player cards, and their values

    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of dealer is {dealer.value}")

    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of player is {player.value}")


"""
END GAME SCENARIOS
"""


def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(dealer, player):
    print("Dealer and player tie! PUSH!")
