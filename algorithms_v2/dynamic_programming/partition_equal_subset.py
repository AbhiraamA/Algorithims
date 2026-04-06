"""
Partition Equal Subset Sum
Time:  O(n * target)
Space: O(target)

Determine if an array can be partitioned into two subsets
with equal sums. Equivalent to finding a subset that sums
to total/2 — a 0/1 knapsack variant.
"""


def can_partition(nums: list) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp     = [False] * (target + 1)
    dp[0]  = True

    for num in nums:
        # Traverse backwards so each num is only used once
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


def partition_subsets(nums: list) -> tuple | None:
    """Returns the two subsets if a valid partition exists, else None."""
    total = sum(nums)
    if total % 2 != 0:
        return None

    target = total // 2
    n      = len(nums)
    dp     = [[False] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]
            if nums[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

    if not dp[n][target]:
        return None

    # Backtrack to find which items go in subset 1
    subset1, j = [], target
    for i in range(n, 0, -1):
        if not dp[i - 1][j]:  # this item was taken
            subset1.append(nums[i - 1])
            j -= nums[i - 1]

    subset2 = nums[:]
    for x in subset1:
        subset2.remove(x)

    return subset1, subset2


if __name__ == "__main__":
    tests = [
        [1, 5, 11, 5],   # True  → [1,5,5] and [11]
        [1, 2, 3, 5],    # False
        [3, 3, 3, 4, 5], # True
    ]
    for nums in tests:
        result = can_partition(nums)
        print(f"  {nums} → {result}")
        if result:
            s1, s2 = partition_subsets(nums)
            print(f"    subsets: {s1} | {s2}")
