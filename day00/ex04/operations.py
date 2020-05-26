#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main(number1: int, number2: int):

    try:
        num1 = int(number1)
        num2 = int(number2)
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        if num2 == 0:
            division = 'ERROR (div by zero)'
            modulo = 'ERROR (modulo by zero)'
        else:
            division = num1 / num2
            modulo = num1 % num2

        print('Sum:         {}'.format(addition))
        print('Difference:  {}'.format(subtraction))
        print('Product:     {}'.format(multiplication))
        print('Quotient:    {}'.format(division))
        print('Remainder:   {}\n'.format(modulo))
    except ValueError as identifier:
        error('only numbers')


def error(msg=None):
    if msg is not None:
        print('InputError: {}\n'.format(msg))
    print('Usage: python operations.py <number1> <number2>\n')
    print('Example:\n')
    print('python operations.py 10 3')


if __name__ == "__main__":
    if len(sys.argv) > 3:
        error('too many arguments')
        exit()
    elif len(sys.argv) < 3:
        error()
        exit()
    main(sys.argv[1], sys.argv[2])
