import pandas as pd

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

try:
    word = input().upper()
    for char in word:
        if not char.isalpha():
             raise ValueError
except ValueError:
    print("The Input Should Contain Alphabet Letters Only.")
else:
    print([dict_nato[char] for char in word])

#Prints Nato Aphabet - using for spelling words on a phone call , to tell spellings of words to others