"""
Linear Search
Time:  O(n)
Space: O(1)

Scans every element until target is found. Works on unsorted
arrays. Optimal when the array is small or data is unordered.
"""

def linear_search(arr: list, target) -> int:
    """Returns the index of target, or -1 if not found."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


if __name__ == "__main__":
    arr = [4, 2, 7, 1, 9, 3]
    print("Array:", arr)
    print("Search 9:", linear_search(arr, 9))
    print("Search 5:", linear_search(arr, 5))
