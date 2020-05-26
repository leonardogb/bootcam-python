#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

morseCode = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
    }


def main(text):
    translation = ''
    wordList = [word.upper() for word in text]

    for x in text:
        if x in morseCode:
            translation += morseCode.get(x) + ' '
        else:
            print('Error')
            sys.exit()
    print(translation)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(sys.argv[1:])
