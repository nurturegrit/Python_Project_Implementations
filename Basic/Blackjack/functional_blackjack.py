#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:30:26 2024

@author: sumit
"""
import random

bet = 0
deck = {}
player_winning = 0

game_logo = " ____    ____    ____    ____\n|2   |  |A   |  |Q   |  |T   |\n|(\/)|  | /\ |  | /\ |  | &  |\n| \/ |  | \/ |  |(__)|  |&|& |\n|   2|  |   A|  | /\Q|  | | T|     BackJack!\n`----`  `----'  `----'  `----'"


def build_deck():
    global deck
    suits = ['Spades','Diamonds','Hearts','Clubs']
    card_dict = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10':10,
        'J': 10,
        'Q': 10,
        'K': 10
    }
    for suit in suits:
        for card,value in card_dict.items():
            deck[f"{card} of {suit}"] = value
    return None

def check_win(player_cards,p_points,d_points):
    """Checks the outcome of the game based on player and dealer hands.

    Args:
        player_cards: List of tuples representing the player's hand (card, value).
        p_points: Player's current point total.
        d_points: Dealer's current point total.

    Returns:
        True if the game is over, False otherwise.
    """
    #Checking for blackjack
    if len(player_cards) == 2 and p_points + 11 == 21 and any('A' in card[0] for card in player_cards):
        print("BlackJack!!! You win!!")
        return True
    #Adusting for Ace in player_cards
    for i, (card,value) in enumerate(player_cards):
        if 'A' in card and p_points + 10 <= 21:
            p_points += 10
            player_cards[i] = (card , p_points)
            break
    #In case of Tie, win through points
    if p_points == d_points:
        print("It is a Tie!")
        return True
    elif p_points > d_points:
        print(f"You wins! with {p_points} points against Dealer's {d_points} points")
    else:
        print(f"Dealer wins! with {d_points} points against your {p_points} points")
    return True

def game_logic(player_cards,dealer_cards):
    global deck
    global bet
    p_points = sum([value for card,value in player_cards])
    d_points = sum([value for card,value in dealer_cards])
    while p_points <= 21 and d_points <= 21:
        #Player_Turn
        Insurance = False
        while True:
            print("Type Integers associated with your choice\n1 - Hit\n2 - Stand\n3 - Calculate\n4 - Surrender\n5 - Insurance\n")
            choice = int(input().strip())
            match choice:
                case 1:#Hit
                    player_cards.append(deck.popitem())
                    p_points += player_cards[-1][1]
                    print("Dealer's cards!")
                    print(dealer_cards[0],'Hidden')
                    print("Player's Cards!")
                    print(player_cards)
                    if p_points > 21:
                        print("You Bust!")
                        bet = 0
                        return False
                case 2:#Stand
                    break
                case 3:#Calculate
                    print("Dealer's cards!")
                    print(dealer_cards[0],'Hidden')
                    print("Player's Cards!")
                    print(player_cards)
                    print(f"You have {p_points} points.")
                    if any('A' in card for card,value in player_cards) and p_points < 17:
                        print("You have an Ace in your hands! Maybe You can hit!")
                    elif p_points < 14:
                        print(f"You have {p_points} points. You have a good chance of a successful hit.")
                case 4:#Surrender
                    print("You Surrendered!")
                    print(f"You have lost ${bet//2} that is half of your bet!")
                    bet -= bet//2
                    return False
                case 5:#Insurance
                    print("You have choosen Insurance!")
                    print("In case the dealer has BlackJack! , You will win 2 times the bet")
                    Insurance = True
                    break
        #Dealer_Turn
        if any('A' in card for card,value in dealer_cards):
            if d_points + 10 <= 21:
                d_points += 10
            if d_points == 21:
                if Insurance:
                    print("You had brought Insurance! and hence won and doubled their bet!!")
                    return True
                else:
                    print("Dealer has BlackJack!")
                    print(f"You lose ${bet} worth of chips!!")
                    return False
        else:
            while d_points < 17:
                print("Dealer hits!")
                dealer_cards.append(deck.popitem())
                d_points += dealer_cards[-1][1]
                if d_points > 21:
                    print('Dealer Busts!')
                    return True
        break #break after dealer's turns
    else:
        if p_points > 21:
            print("Player Busts!")
            return False
        else:
            print('Dealer Busts!')
            return True
    return check_win(player_cards,p_points,d_points)

def welcome():
    global player_winning
    global bet
    global deck
    print(game_logo)
    print("Welcome to the Game of BlackJack!")
    chips = input("Would you like to add chips? Y/n\n").lower()
    if chips == 'y':
        bet += int(input("Type Amount of chips you want to add in dollars.\n").lower())    
    build_deck()
    dealer_cards = []
    player_cards = []
    temp_list = list(deck.keys())
    random.shuffle(temp_list)
    deck = {key: deck[key] for key in temp_list}
    for _ in range(2):
        player_cards.append(deck.popitem())
        dealer_cards.append(deck.popitem())
    print("Dealer's cards!")
    print(dealer_cards[0],'Hidden')
    print("Player's Cards!")
    print(player_cards)
    win = game_logic(player_cards,dealer_cards)
    if win:
        player_winning += 1
        bet += bet
    else:
        player_winning -= 1
        bet -= bet
    print(f"Your Final Score is {player_winning} with the current chips of value ${bet}")
    again = input("Play Again? Y/n\n").lower()
    if again == 'y':
        welcome()
    return None

if __name__ == '__main__':
    welcome()