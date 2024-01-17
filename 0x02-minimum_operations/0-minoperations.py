#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Minimum Operations """
    if n <= 1:
        return 0
    x = 2
    y = 0
    while x <= n:
        if n % x == 0:
            y += x
            n = n / x
        else:
            x += 1
    return y
