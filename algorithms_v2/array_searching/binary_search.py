"""
Binary Search
Time:  O(log n)
Space: O(1) iterative | O(log n) recursive
Requires: sorted array

Repeatedly halves the search space by comparing the target
to the middle element. The go-to for sorted arrays.
"""

def binary_search(arr: list, target) -> int:
    """Iterative. Returns index of target or -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def binary_search_recursive(arr: list, target, lo: int = 0, hi: int = None) -> int:
    """Recursive variant."""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    return binary_search_recursive(arr, target, lo, mid - 1)


def first_occurrence(arr: list, target) -> int:
    """Returns index of the first occurrence of target."""
    lo, hi, result = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid; hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


def last_occurrence(arr: list, target) -> int:
    """Returns index of the last occurrence of target."""
    lo, hi, result = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            result = mid; lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return result


if __name__ == "__main__":
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Array:", arr)
    print("Binary search 23:      index", binary_search(arr, 23))
    print("Binary search (rec) 23: index", binary_search_recursive(arr, 23))
    dupes = [1, 2, 2, 2, 3, 4]
    print("\nDupes:", dupes, "target=2")
    print("First occurrence:", first_occurrence(dupes, 2))
    print("Last occurrence: ", last_occurrence(dupes, 2))
