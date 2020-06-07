"""Solution to 8.11 Coins.

Given an infinite number of quarters (25 cents), dimes (10 cents),
nickles (5 cents), and pennies (1 cent), write code to calculate the
number of ways of representing `n` cents.
"""


def coin_combinations(n: int) -> int:
    """Returns the number of ways of representing n cents.

    Representations of cents can include any number of quarters (25
    cents), dimes (10 cents), nickles (5 cents), and pennies (1 cent).
    """
    if n < 0:
        return 0
    dp = [1] + [0] * n
    for coin in [1, 5, 10, 25]:
        for i in range(len(dp) - coin):
            dp[i + coin] += dp[i]
    return dp[-1]
