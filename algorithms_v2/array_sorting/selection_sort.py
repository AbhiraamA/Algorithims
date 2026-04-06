"""
Selection Sort
Time:  O(n²)
Space: O(1)
Stable: No

Finds the minimum element from the unsorted portion and
swaps it into the correct position. Always makes exactly
n-1 swaps regardless of input — good when writes are costly.
"""

def selection_sort(arr: list) -> list:
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    test = [64, 25, 12, 22, 11]
    print("Input: ", test)
    print("Output:", selection_sort(test))
