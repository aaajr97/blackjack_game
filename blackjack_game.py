from blackjack_classes_and_functions import *
import blackjack_classes_and_functions
playing = True

while True:
    # Opening statement
    print('B L A C K J A C K')

    # Create a deck, shuffle it and deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up player's chips
    player_chips = Chips()

    # Prompts player to place a bet
    take_bet(player_chips)

    # Show cards (keeps one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while blackjack_classes_and_functions.playing:
        # Prompts player to hit or stand
        hit_or_stand(deck, player_hand)

        # Show cards (keeps one dealer card hidden)
        show_some(player_hand, dealer_hand)

    # If value of player's hands exceeds 21, run player_bust() and exit loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If player has not busted, play dealers hand until it reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run various end-game scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Informs player of their chips total
    print('\n Player total chips are at: {}'.format(player_chips.total))

    # Ask to play again
    new_game = input("Play another game? y/n: ")

    if new_game[0].lower() == 'y':
        blackjack_classes_and_functions.playing = True
        continue
    else:
        print('Thanks for playing!')
        break
