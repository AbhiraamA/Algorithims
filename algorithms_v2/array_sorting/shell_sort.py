"""
Shell Sort
Time:  O(n log² n) — depends on gap sequence
Space: O(1)
Stable: No

Generalization of insertion sort. Sorts elements far apart
first, gradually reducing the gap. Much faster than insertion
sort for larger arrays.
"""

def shell_sort(arr: list) -> list:
    arr = arr[:]
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


if __name__ == "__main__":
    test = [12, 34, 54, 2, 3]
    print("Input: ", test)
    print("Output:", shell_sort(test))
