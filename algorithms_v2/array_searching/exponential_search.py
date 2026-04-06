"""
Exponential Search
Time:  O(log n)
Space: O(1)
Requires: sorted array

Finds the range where the target exists by doubling the index
(1, 2, 4, 8...), then runs binary search within that range.
Ideal for unbounded/infinite sorted arrays.
"""

def exponential_search(arr: list, target) -> int:
    """Returns index of target or -1."""
    n = len(arr)
    if not n:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    lo = i // 2
    hi = min(i, n - 1)
    return _binary_search(arr, target, lo, hi)


def _binary_search(arr, target, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 55, 78, 99, 120]
    print("Array:", arr)
    print("Search 10:", exponential_search(arr, 10))
    print("Search 50:", exponential_search(arr, 50))
