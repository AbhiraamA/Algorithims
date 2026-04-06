"""
Bubble Sort
Time:  O(n²)
Space: O(1)
Stable: Yes

Repeatedly swaps adjacent elements that are out of order.
Best case O(n) with early exit optimization (already sorted).
"""

def bubble_sort(arr: list) -> list:
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # already sorted — early exit
            break
    return arr


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Input: ", test)
    print("Output:", bubble_sort(test))
