#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:11:01 2024

@author: sumit
"""

import csv
import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def extract_data():
    data = {}
    with open("instagram_top_1000.csv",'r') as file:
        reader = csv.DictReader(file, fieldnames=['Country', 'Rank', 'Account', 'Title', 'Link', 'Category', 'Followers', 'Audience Country', 'Authentic engagement', 'Engagement avg', 'Scraped'])
        for line in reader:
            data[f"{line['Title']} of Category {line['Category']}"] = line['Rank']
    return data

def game():
    logo='''////////////////////////////////////////////////////////////////
// _   _ _       _                ___                         //
//| | | (_) __ _| |__   ___ _ __ / / | _____      _____ _ __  //
//| |_| | |/ _` | '_ \ / _ \ '__/ /| |/ _ \ \ /\ / / _ \ '__| //
//|  _  | | (_| | | | |  __/ | / / | | (_) \ V  V /  __/ |    //
//|_| |_|_|\__, |_| |_|\___|_|/_/  |_|\___/ \_/\_/ \___|_|    //
//         |___/                                              //
////////////////////////////////////////////////////////////////'''
    versus = '''oooooo     oooo         
 `888.     .8'          
  `888.   .8'    .oooo.o
   `888. .8'    d88(  "8
    `888.8'     `"Y88b. 
     `888'      o.  )88b
      `8'       8""888P'''
    data = extract_data()
    keys = list(data.keys())
    play = True
    p_points = 0
    while play:
        clear_console()
        print(logo)
        char1 = random.choice(keys)
        char2 = random.choice(keys)
        if char1 == char2:
            continue
        print("Choose Between The Following!")
        print(f" 1 {char1} \n{versus}\n 2 {char2} \n")
        choice = int(input())
        if choice == 1 and data[char1] < data[char2]:
            print("You are right!")
            print("Player_points + 10")
            p_points += 10
        else:
            print("You are wrong!")
            print("Player_points - 10")
            p_points -= 10
        print(f"You have {p_points} points currently.")
        again = input("Do you want to guess again? Y/n\n").lower()
        if again == 'y':
            continue
        else:
            return p_points
        
def main():
    print("Welcome to the game of Higher/Lower. Instagram version.")
    print("Rules:- In this game , you will be provided with name of 2 Instagram Influencers/Celebritties.")
    print("You have to guess which one is higher")
    points = game()
    if points < 0:
        print("You lost!")
    else:
        if points > 1000:
            print(f"You are incredible!. You earned {points} points.")
            print("You won.")
        elif points > 100:
            print(f"You are good. You made {points} points")
            print("You won.")
        else:
            print("You won.")
    return True
    

if __name__ == '__main__':
    cont = True
    while cont:
        main()
        again = input("Do you want to play again? Y/n\n").lower()
        if again != 'y':
            cont = False