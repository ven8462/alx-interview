#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ Minimum Operations"""
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 2)
        dp[i] = min(dp[i], dp[i-1] + 1)
    return dp[n] if dp[n] != float('inf') else 0
