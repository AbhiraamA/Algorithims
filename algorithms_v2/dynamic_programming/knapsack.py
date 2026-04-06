"""
0/1 Knapsack
Time:  O(n * W)  — n items, W capacity
Space: O(W)  — space-optimized with 1D array

Each item can be taken at most once. Maximize total value
without exceeding the weight capacity.
"""


def knapsack(weights: list, values: list, capacity: int) -> int:
    n  = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Traverse backwards to avoid using item i twice
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


def knapsack_with_items(weights: list, values: list, capacity: int) -> tuple:
    """Returns (max_value, list_of_chosen_item_indices)."""
    n  = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # Backtrack to find chosen items
    chosen, w = [], capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], chosen[::-1]


if __name__ == "__main__":
    weights  = [1, 3, 4, 5]
    values   = [1, 4, 5, 7]
    capacity = 7

    print(f"Weights:  {weights}")
    print(f"Values:   {values}")
    print(f"Capacity: {capacity}")
    print(f"Max value:         {knapsack(weights, values, capacity)}")
    val, items = knapsack_with_items(weights, values, capacity)
    print(f"Max value (items): {val}, chosen item indices: {items}")
