#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    time = (3, 30, 2019, 9, 25)
    print('{0[3]:02}/{0[4]:02}/{0[2]} {0[0]:02}:{0[1]:02}'.format(time))


if __name__ == "__main__":
    main()
