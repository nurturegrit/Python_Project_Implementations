#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:41:07 2024

@author: sumit
"""
from string import ascii_lowercase as alpha

alphabet = list(alpha)


def code(jump,letter,function):
    global aphabet
    i = alphabet.index(letter)
    if function == 'encrypt':
        i = (i + jump) % 26
    if function == 'decrypt':
        i = (i - jump) % 26
    return alphabet[i]


    
def main():
    print("This Program will take alphabet words as input and encrypt/decrypt them")
    direction = input("Choose 'encrypt'/'decrypt'\n").lower().strip()
    if direction not in ['encrypt','decrypt']:
        print("Choose Correctly! ")
        main()
    shift = int(input("Enter the Shift Number (Integer)\n"))
    message = input("Enter the Message.\n")
    result =  ''
    for char in message:
        if char in alphabet:
            result += code(shift,char,direction)
            continue
        result += char
    print(result)
    choice = input("Do you want to go again? Y/n\n").lower().strip()
    if choice == 'y':
        main()
if __name__ == '__main__':
    print('''╔═══╗                         ╔═══╗      ╔╗         
║╔═╗║                         ║╔═╗║      ║║         
║║ ╚╝╔══╗ ╔══╗╔══╗╔══╗ ╔═╗    ║║ ╚╝╔╗╔══╗║╚═╗╔══╗╔═╗
║║ ╔╗╚ ╗║ ║╔╗║║══╣╚ ╗║ ║╔╝    ║║ ╔╗╠╣║╔╗║║╔╗║║╔╗║║╔╝
║╚═╝║║╚╝╚╗║║═╣╠══║║╚╝╚╗║║     ║╚═╝║║║║╚╝║║║║║║║═╣║║ 
╚═══╝╚═══╝╚══╝╚══╝╚═══╝╚╝     ╚═══╝╚╝║╔═╝╚╝╚╝╚══╝╚╝ 
                                     ║║             
                                     ╚╝             
''')
    main()