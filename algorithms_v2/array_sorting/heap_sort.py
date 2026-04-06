"""
Heap Sort
Time:  O(n log n) — all cases
Space: O(1)
Stable: No

Builds a max-heap in-place, then repeatedly extracts the max
element to the end of the array. Combines the space efficiency
of selection sort with the time efficiency of merge sort.
"""

def heap_sort(arr: list) -> list:
    arr = arr[:]
    n = len(arr)

    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

    return arr


def _heapify(arr: list, n: int, i: int):
    largest = i
    left  = 2 * i + 1
    right = 2 * i + 2

    if left  < n and arr[left]  > arr[largest]: largest = left
    if right < n and arr[right] > arr[largest]: largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


if __name__ == "__main__":
    test = [12, 11, 13, 5, 6, 7]
    print("Input: ", test)
    print("Output:", heap_sort(test))
