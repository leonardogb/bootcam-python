#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text."""
    total = 0
    uppercases = 0
    lowercases = 0
    punctuations = 0
    spaces = 0
    if len(args) < 2:
        if len(args) == 0:
            tmp = input('What is the text to analyse?\n')
            if isinstance(tmp, str) is True:
                text = tmp
            else:
                print('Error')
                return None
        elif len(args) == 1:
            tmp = args[0]
            if isinstance(tmp, str) is True:
                text = tmp
            else:
                print('Error')
                return None

        if text is None:
            text = input('What is the text to analyse?\n')
        for c in text:
            if c.isupper() is True:
                uppercases += 1
            elif c.islower() is True:
                lowercases += 1
            elif c in string.punctuation:
                punctuations += 1
            elif c == ' ':
                spaces += 1
            total += 1
        print('The text contains {} characters\n'.format(total))
        print('- {} upper letters\n'.format(uppercases))
        print('- {} lower letters\n'.format(lowercases))
        print('- {} punctuation marks\n'.format(punctuations))
        print('- {} spaces'.format(spaces))
    else:
        print('Error')
