#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for key in languages:
        print('{} was created by {}'.format(key, languages[key]))


if __name__ == "__main__":
    main()
