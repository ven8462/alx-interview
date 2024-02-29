#!/usr/bin/python3
"""
making change module
"""


def makeChange(coins, total):
    """
    determines the fewest number of coins to make change
    """
    if total <= 0:
        return 0
    if len(coins) is 0:
        return -1
    coins = sorted(coins)
    change_dynamic = [float('inf')] * (total + 1)
    change_dynamic[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                break
            if change_dynamic[i - coin] != -1:
                change_dynamic[i] = min(change_dynamic[i - coin] + 1, change_dynamic[i])
    if change_dynamic[total] == float('inf'):
        return -1
    return change_dynamic[total]
