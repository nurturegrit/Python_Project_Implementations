#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 13:14:19 2024

@author: sumit
"""

import random

def main():
    print("Welcome to play Rock Paper Scissors!")
    options = ['Rock','Paper','Scissors']
    while True:
        player = input("Input Rock|Paper|Scissors  ").strip().lower().capitalize()
        computer = random.choice(options)
        print("You PLayed",player)
        print("Computer Played", computer)
        if player == computer:
            print("It's a Tie!!")
        elif player == 'Scissors' and computer =='Paper':
            print("Player Wins!")
        elif player == 'Paper' and computer =='Rock':
            print("Player Wins!!")
        elif player == 'Rock' and computer =='Scissors':
            print("Player Wins!!")
        elif player not in options:
            print("Input a correct choice.")
        else:
            print("Computer Wins!")
        if 'q' == input("Enter 'q'/'Q' to Quit!").strip().lower():
            break

main()