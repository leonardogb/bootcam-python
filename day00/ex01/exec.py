#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Reverses the order of a string and the case of its word'
        )
    parser.add_argument('words', nargs='+', type=str,
                        help='a word or a list of words')
    args = parser.parse_args()
    listWords = []
    text = ''

    for value in args.words:
        words = value.split()
        for word in words:
            listWords.insert(0, word[::-1].swapcase())

    for index, word in enumerate(listWords):
        if index > 0:
            text += ' '
        text += word

    print(text)


if __name__ == "__main__":
    main()
