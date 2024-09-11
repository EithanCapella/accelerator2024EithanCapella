"""

Consider a row of coins, each with a different value. The number of coins is even. We play a game against an opponent by
alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row
permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if
we move first. You should assume that you will go first, and that the opponent is as clever as you are (that is, the
opponent is also trying to maximize their winnings).

HINT: This is a "zero-sum" game - in other words, maximizing the value of the coins you select is the same as minimizing
the value of the coins your opponent selects (and the same is true for your opponent). Therefore you can think of the
opponent's move as the one that minimizes the value that you can get.

"""
from typing import List


def max_coin_game(coins: List[int]) -> int:
    """

    This function accepts a list of numbers that gives the values of coins, and returns the maximum amount the first
    player can win playing the game according to the rules explained above.

    Parameters
    ----------

    coins: List[int]
        A list of integers that gives the values of coins.

    Returns
    -------

    int
        The maximum amount the first player can win.

    """
    result = 0
    #
    # YOUR CODE GOES HERE
    #
    return result


#
# TESTS
#
coins = [1, 5, 10, 1]
expected = 11
result = max_coin_game(coins)
assert expected == result, f"Wrong result with input: {coins}"

coins = [10, 5, 1, 25, 5, 5]
expected = 40
result = max_coin_game(coins)
assert expected == result, f"Wrong result with input: {coins}"

coins = [10, 5, 1, 25, 5, 5, 10, 5, 1, 25, 5, 5]
expected = 75
result = max_coin_game(coins)
assert expected == result, f"Wrong result with input: {coins}"
