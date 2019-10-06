from cards import Chips, Card, Deck, Hand

player_chips = Chips()

def take_bet():
    waiting = True
    while waiting:
        try:
            bet = int(input("How much do you want to bet?"))
            if bet <= player_chips.total:
                waiting = False

            else:
                print("sorry you do not have enough")
                continue
        except:
            print("Sorry just type a number for how many chips you wnat to bet")
            continue


    print(f"thank you, you bet {bet} chips!!")

deck=Deck()
hand = Hand()

def hit(deck, hand):
    card = Deck.deal(deck)
    Hand.add_cards(hand, card)
    if hand.value > 21 :
        if hand.aces > 0 :
            hand.adjust_for_ace(hand)
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
