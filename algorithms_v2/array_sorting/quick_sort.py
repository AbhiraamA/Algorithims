"""
Quick Sort
Time:  O(n log n) avg | O(n²) worst (bad pivot)
Space: O(log n) — call stack
Stable: No

Picks a pivot, partitions the array so elements less than the
pivot are left and greater are right, then recurses on both
sides. Fastest in practice for most inputs due to cache locality.
"""

def quick_sort(arr: list) -> list:
    arr = arr[:]
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr: list, low: int, high: int):
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort(arr, low, pi - 1)
        _quick_sort(arr, pi + 1, high)


def _partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    test = [10, 7, 8, 9, 1, 5]
    print("Input: ", test)
    print("Output:", quick_sort(test))
