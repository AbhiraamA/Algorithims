"""
House Robber
Time:  O(n)
Space: O(1)

Can't rob two adjacent houses. At each house decide: skip it,
or rob it (adding the value from two houses back).
"""


def rob(nums: list) -> int:
    """Maximum money you can rob from a row of houses."""
    prev = curr = 0
    for n in nums:
        prev, curr = curr, max(curr, prev + n)
    return curr


def rob_circular(nums: list) -> int:
    """House Robber II — houses arranged in a circle.
    First and last houses are adjacent, so we run rob() twice:
    once excluding the last house, once excluding the first.
    """
    if len(nums) == 1:
        return nums[0]

    def rob_range(houses):
        prev = curr = 0
        for n in houses:
            prev, curr = curr, max(curr, prev + n)
        return curr

    return max(rob_range(nums[:-1]), rob_range(nums[1:]))


if __name__ == "__main__":
    tests = [
        [1, 2, 3, 1],    # 4  (rob 1 and 3)
        [2, 7, 9, 3, 1], # 12 (rob 2, 9, 1)
        [2, 3, 2],        # circular → 3
        [1, 2, 3, 1],    # circular → 4
    ]
    print("Linear:")
    for t in tests[:2]:
        print(f"  {t} → {rob(t)}")

    print("Circular:")
    for t in tests[2:]:
        print(f"  {t} → {rob_circular(t)}")
