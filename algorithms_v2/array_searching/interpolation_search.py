"""
Interpolation Search
Time:  O(log log n) avg for uniformly distributed data | O(n) worst
Space: O(1)
Requires: sorted array

Like binary search but estimates the probe position using
linear interpolation. Faster than binary search when values
are uniformly distributed (e.g. phone book lookups).
"""

def interpolation_search(arr: list, target) -> int:
    """Returns index of target or -1."""
    lo, hi = 0, len(arr) - 1

    while lo <= hi and arr[lo] <= target <= arr[hi]:
        if arr[lo] == arr[hi]:
            return lo if arr[lo] == target else -1

        # Estimate position via linear interpolation
        pos = lo + ((target - arr[lo]) * (hi - lo) // (arr[hi] - arr[lo]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Array:", arr)
    print("Search 70:", interpolation_search(arr, 70))
    print("Search 45:", interpolation_search(arr, 45))
