#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Check if a number is odd, even or zero'
        )
    parser.add_argument('number', type=int,
                        help='a integer')

    number = parser.parse_args().number

    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
