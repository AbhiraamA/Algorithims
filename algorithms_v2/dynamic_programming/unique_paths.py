"""
Unique Paths
Time:  O(m * n)
Space: O(n)  — space-optimized with 1D array

Count the number of unique paths from the top-left to the
bottom-right of an m x n grid, moving only right or down.
"""


def unique_paths(m: int, n: int) -> int:
    """Returns number of unique paths in an m×n grid."""
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]


def unique_paths_with_obstacles(grid: list) -> int:
    """Grid has obstacles (1 = blocked, 0 = open).
    Time: O(m*n)  Space: O(n)
    """
    m, n = len(grid), len(grid[0])
    dp   = [0] * n
    dp[0] = 1 if grid[0][0] == 0 else 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]

    return dp[-1]


if __name__ == "__main__":
    print("Unique paths 3×7:", unique_paths(3, 7))   # 28
    print("Unique paths 3×2:", unique_paths(3, 2))   # 3

    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    print("With obstacle:   ", unique_paths_with_obstacles(grid))  # 2
