#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    t = (0, 4, 132.42222, 10000, 12345.67)
    day = 'day_{0[0]:02}'.format(t)
    exe = 'ex_{0[1]:02}'.format(t)
    num1 = '{0[2]:.2f}'.format(t)
    num2 = '{0[3]:.2e}'.format(t)
    num3 = '{0[4]:.2e}'.format(t)
    print('{}, {} : {}, {}, {}'.format(day, exe, num1, num2, num3))


if __name__ == "__main__":
    main()
# day_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
