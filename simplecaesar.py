 #!/usr/bin/env python
# This is a program for executing the Caesar cipher of shifing charcters
# 3 places alphabetically

import string
from string import *
from random import randint
import os
from os import chdir
from os import getcwd
from os import listdir

def encode(text):

    converted = ''
    for letter in text:
        if letter == ' ':
            converted = converted + ' '
        else:
            x = letters.index(letter) + shift
            converted = converted + letters[x]
    return converted

def decode(text):
    converted = ''
    for letter in text:
        if letter == ' ':
            converted = converted + ' '
        else:
            X = letters.index(letter) - shift
            converted = converted + letters[X]
    return converted

def do_nothing():
	x = getcwd()
	x = listdir(x)


shift = 3
converted = ''
flag1 = True
FLAG2 = False
flag3 = False
letters = string.ascii_letters + string.punctuation + string.digits

if __name__ == '__main__':
    while True:
        choice = input("\tWould you like to encode, decode or quit?").lower()
        converted = ''
        if choice == "encode":
            converted = encode(input('Enter text to encode:'))
        elif choice == "decode":
            converted = decode(input('Enter text to decode:'))
        elif choice == 'quit':
            break
        else:
            print(choice, 'is unknown command. Please enter a supported one.')
            continue
            print('out of here')
        print('Conversion:', converted)
        if not flag1:
            print('dead')
        continue
        do_nothing()

    if FLAG2 == True:
        print('more dead')
