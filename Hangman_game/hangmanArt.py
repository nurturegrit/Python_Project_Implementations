#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:21:48 2024

@author: sumit
"""
logo = '''  |   |                                               
  |   |   _` |  __ \    _` |  __ `__ \    _` |  __ \  
  ___ |  (   |  |   |  (   |  |   |   |  (   |  |   | 
 _|  _| \__,_| _|  _| \__, | _|  _|  _| \__,_| _|  _| 
                      |___/                           '''
#Hangmen Game Ascii Art
stages = ['''  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']