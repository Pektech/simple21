from cards import Card, Deck, Hand, Chips
from game_functions import *

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    # set up players ships
    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    hit_or_stand(deck, player_hand)

    show_some(player_hand, dealer_hand)

    if player_hand.value >21:
        player_busts(player_hand, dealer_hand,player_chips)
        break
    if player_hand.value <=21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break