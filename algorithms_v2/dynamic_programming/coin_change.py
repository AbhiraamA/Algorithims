"""
Coin Change — Minimum Coins
Time:  O(n * amount)
Space: O(amount)

Given coin denominations and a target amount, find the fewest
coins needed to make that amount. Each coin can be used unlimited
times (unbounded knapsack variant).
"""


def coin_change(coins: list, amount: int) -> int:
    """Returns minimum number of coins, or -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins: list, amount: int) -> int:
    """Returns the number of combinations that make up amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


if __name__ == "__main__":
    tests = [
        ([1, 5, 6, 9], 11),   # min coins = 2 (5+6)
        ([1, 2, 5], 11),       # min coins = 3 (5+5+1)
        ([2], 3),              # impossible = -1
        ([1], 0),              # 0 coins
    ]
    for coins, amount in tests:
        result = coin_change(coins, amount)
        ways   = coin_change_ways(coins, amount)
        print(f"  coins={coins}, amount={amount}  →  min coins={result}, ways={ways}")
