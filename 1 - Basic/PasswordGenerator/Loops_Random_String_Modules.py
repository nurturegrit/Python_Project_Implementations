#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 14:06:43 2024

@author: sumit
"""
import string , random
characters = list(string.ascii_letters)
numbers = list(string.digits)
special_symbol = list(string.punctuation)

password = []
n = int(input("How many letters in a password?"))
for i in range(int(input("How many characters in the password"))):
    password.append(random.choice(characters))
for i in range(int(input("How many numbers in the password"))):
    password.append(random.choice(numbers))
while len(password) < n:
    password.append(random.choice(special_symbol))

random.shuffle(password)

password = ''.join(password)

print(password)