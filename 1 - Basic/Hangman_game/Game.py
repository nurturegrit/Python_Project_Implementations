#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:30:29 2024

@author: sumit
"""

import random
import os
from hangmanArt import stages , logo

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    words_list = ['writing', 'footnote', 'glorious', 'seventeen', 'sequence', 'clinical', 'favorite', 'suddenly', 'society', 'variety']

    chosen_word = [char for char in random.choice(words_list)]
    print(logo)
    print("Welcome to the Hangman Game!")
    print(''' Rules:-
          You only have 5 chances to guess the wromg character.
          Before that You have to guess the word correctly.
          Otherwise , You will not be able to save the Hanging Man!!
          He will Die!! Help Him by doing your best!''')
    won = game(chosen_word)
    if won:
        print("Hurray!! , You have saved a life!")
    else:
        print("The word was "+''.join(chosen_word))
        print("The Hanged Man is Dead!")
      
def game(word):
    blanks = ['_' for i in range(len(word))]
    lives = 6
    print(stages[0])
    while lives > 0 and '_' in blanks:
        print(''.join(blanks))
        guess = input("Guess a character in the above word! ").strip().lower()
        if guess in blanks:
            print("The character",guess, "is already guessed")
        elif guess in word:
            while guess in word:
                index = word.index(guess)
                blanks[index] = guess
                word[index] = '-'
        else:
            lives -= 1
            clear_console()
            print(stages[6-lives])
            print(f"You have {lives} lives left!")
    if '_' in blanks:
        return False
    else:
        return True

if __name__ == '__main__':
    main()