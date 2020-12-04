#!/usr/bin/env python
# This is a program for executing the Caesar cipher of shifing charcters
# 3 places alphabetically

from simplecaesar import decode, encode
from random import randint



shift = 3
converted = ''
flag1 = True
flag2 = False
flag3 = False


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

    if flag2 is True:
        print('more dead')
