import random


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


def deal():
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 1:
            card = "A"
        hand.append(card)
    return hand


def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 1:
        card = "A"
    hand.append(card)
    return hand


def total(hand):
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score = score + 10
        elif card == "A":
            if score >= 11:
                score = score + 1
            else:
                score += 11
        else:
            score += card
    return score


def play_again():
    again = input("Would you like to play again?(Y/N): ")
    if again == "y" or again == "Y":
        # game()
        return
    else:
        print("Thank you for your hard work!")
        exit()


def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(
            f"\n Dealer total{total(dealer_hand)}Your total{total(player_hand)}is.\033[32mYOU WIN!\033[0m")
    elif total(dealer_hand) > total(player_hand):
        print(
            f"\n Dealer total{total(dealer_hand)}Your total{total(player_hand)}is.\033[91mYOU LOSE...\033[0m")


def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"The dealer's card is{dealer_hand[0]}is.")
    print(f"The player's card is{player_hand}The total is{total(player_hand)}is.")

    choice = 0

    while choice != quit:
        choice = input("Do you want to hit? Do you want to stand?(HIT/STAND): ").lower()
        if choice == "hit":
            hit(player_hand)
            print(
                f"\n to you{player_hand[-1]}Is dealt and the card is{player_hand}The total is{total(player_hand)}is.")
            if total(player_hand) > 21:
                print("You have exceeded 21.\033[91mYOU LOSE...\033[0m")
                choice = quit

        elif choice == "stand":
            print(
                f"\n The dealer's second card is{dealer_hand[1]}The total is{total(dealer_hand)}is.")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(
                    f"To the dealer{dealer_hand[-1]}Is dealt and the card is{dealer_hand}The total is{total(dealer_hand)}is.")
                if total(dealer_hand) > 21:
                    print("The number of dealers has exceeded 21.\033[32mYOU WIN!\033[0m")
                    choice = quit

            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                choice = quit


game()
