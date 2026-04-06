"""
Longest Increasing Subsequence (LIS)
Time:  O(n log n)  — patience sort with binary search
Space: O(n)

Finds the length of the longest strictly increasing subsequence.
The patience sort approach maintains a list of "pile tops" and
uses binary search to find where each element fits.
"""

import bisect


def lis_length(nums: list) -> int:
    """Returns the length of the LIS."""
    tails = []
    for n in nums:
        pos = bisect.bisect_left(tails, n)
        if pos == len(tails):
            tails.append(n)
        else:
            tails[pos] = n
    return len(tails)


def lis_sequence(nums: list) -> list:
    """Returns one actual LIS — O(n log n) time."""
    if not nums:
        return []
    n      = len(nums)
    tails  = []
    index  = []   # index into nums for each tail
    parent = [-1] * n

    for i, num in enumerate(nums):
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
        index.append(pos)
        parent[i] = index[pos - 1] if pos > 0 else -1

    # Backtrack to reconstruct sequence
    seq = []
    idx = index.index(len(tails) - 1)  # last element of LIS
    while idx != -1:
        seq.append(nums[idx])
        idx = parent[idx]

    return seq[::-1]


if __name__ == "__main__":
    tests = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7],
        [1, 2, 3, 4, 5],
    ]
    for nums in tests:
        print(f"  {nums}")
        print(f"    length={lis_length(nums)}, sequence={lis_sequence(nums)}")
