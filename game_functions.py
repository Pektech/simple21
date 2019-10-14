from cards import Chips, Card, Deck, Hand

player_chips = Chips()

def take_bet(chips):
    waiting = True
    while waiting:
        try:
            chips.bet = int(input("How much do you want to bet?"))
            if chips.bet <= player_chips.total:
                waiting = False

            else:
                print("sorry you do not have enough")
                continue
        except:
            print("Sorry just type a number for how many chips you wnat to bet")
            continue


    print(f"thank you, you bet {chips.bet} chips!!")

deck=Deck()
hand = Hand()

def hit(deck, hand):
    card = Deck.deal(deck)
    Hand.add_cards(hand, card)
    if hand.value > 21 :
        if hand.aces > 0 :
            hand.adjust_for_ace()
        else :
            print('bust')

    print(hand)


def hit_or_stand(deck,hand):
    playing = True
    while playing:
        try:
            player_input = input("you have cards. Do you want to stand or hit")
            if player_input == 'hit' :
                hit(deck, hand)
            elif player_input == 'stand' :
                print('standing')
                playing = False
        except:
            print("just type hit for another card or stand to stop")
            continue


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden> ")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")