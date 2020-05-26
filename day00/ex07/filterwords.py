#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import string


def main(lista, length):
    wordsList = lista.translate(
        str.maketrans('', '', string.punctuation)
        ).split()
    max = None
    if length.isdigit():
        max = int(length)
    if len(wordsList) > 0 and max is not None:
        newList = [word for word in wordsList if len(word) > max]
        print(newList)
    else:
        print('\033[1;31mError\033[0;0m')


if __name__ == "__main__":
    if len(sys.argv) == 3 and not sys.argv[1].isdigit():
        main(sys.argv[1], sys.argv[2])
    else:
        print('\033[1;31mError\033[0;0m')
