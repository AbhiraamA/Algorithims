"""
Insertion Sort
Time:  O(n²) worst | O(n) best (nearly sorted)
Space: O(1)
Stable: Yes

Builds the sorted array one element at a time by inserting
each new element into its correct position. Excellent for
small or nearly-sorted datasets; used as base case in Timsort.
"""

def insertion_sort(arr: list) -> list:
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    test = [12, 11, 13, 5, 6]
    print("Input: ", test)
    print("Output:", insertion_sort(test))
