#!/usr/bin/python3
"""
function makeChange
"""


def makeChange(coins, total):
    """
    Returns: least number of coins needed to meet total
        If total <= 0, return 0
        If total cant be met by any number if coins I have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coins <= total:
            total -= coin
            change += 1
            if (total == 0):
                return change
    return -1
