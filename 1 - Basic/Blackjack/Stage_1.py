#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:53:21 2024

@author: sumit
"""
import random

logo = " ____    ____    ____    ____\n|2   |  |A   |  |Q   |  |T   |\n|(\/)|  | /\ |  | /\ |  | &  |\n| \/ |  | \/ |  |(__)|  |&|& |\n|   2|  |   A|  | /\Q|  | | T|     BackJack!\n`----`  `----'  `----'  `----'"

def build_deck():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    card_values = {
        "A": 1,  # Ace
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "J": 10,  # Jack
        "Q": 10,  # Queen
        "K": 10,  # King
    }

    deck = {}
    for suit in suits:
        for value, number in card_values.items():
            card = f"{value}{suit}"  # Combine value and suit
            deck[card] = number
    return deck

def game(player1,player2):
    p1_points = player1[0][1] + player1[1][1]
    p2_points = player2[0][1] + player2[1][1]
    print("The Cards are Distributed")
    j = i = 2
    while p1_points < 21 and p2_points < 21:
        print("Check Your Cards")
        print(player2[:2]) #Your Cards
        print(player1[:2]) #Computer Cards
        p2_choice = int(input("1 Stand\n2 Hit\n3 Calculate\n"))
        if p2_choice == '1':
            pass
        elif p2_choice == '2':
            print(player2[:i+1])
            p2_points += player2[i][1]
            i += 1
        else:
            print(p2_points)
        p1_choice = random.randint(1,3)
        if p1_choice == '1':
            pass
        elif p1_choice == '2':
            p1_points += player1[j][1]
            j += 1
        else:
            continue
    for _ in range(i):
        if 'A' in player1[i][0]:
            p1_points += 10
        if 'A' in player2[i][0]:
            p2_points += 10
        
    if p1_points == p2_points:
        print("It's a Tie")
        return None
    elif p1_points > p2_points:
        print("Computer Wins!")
        return False
    else:
        print("You Win!!")
        return True
        
def main(): 
    print(logo)
    print("Welcome to the game of Blackjack")
    choice = input("Do you want to play? Y/n").lower().strip()
    if choice != 'y':
        return None
    computer_cards = []
    player_cards = []
    card_deck = build_deck()
    for _ in range(6): #Shuffling and assigning cards
        temp_list = list(card_deck.keys())
        random.shuffle(temp_list)
        card_deck = {key: card_deck[key] for key in temp_list}
        computer_cards.append(card_deck.popitem())
        player_cards.append(card_deck.popitem())
    game(computer_cards,player_cards)
    

main()
    