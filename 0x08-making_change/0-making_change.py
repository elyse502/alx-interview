#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    Dyanimc Programmming Bottom Up Solution
    """
    if total <= 0:
        return 0
    # Initialize list with maximum amount(which cannot be reached)
    # This helps to calculate a new minimum
    # E.G: If total = 2, list = [3,3,3]
    dp = [total + 1] * (total + 1)
    # Set minimum number of coins for amount 0
    dp[0] = 0

    # Start from 1 because we know dp[0]
    for amount in range(1, total + 1):
        # test for every coin
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return dp[total] if dp[total] != total + 1 else -1
