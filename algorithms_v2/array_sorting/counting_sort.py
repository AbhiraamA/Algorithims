"""
Counting Sort
Time:  O(n + k)  — k = range of values
Space: O(k)
Stable: Yes

Non-comparison sort. Counts occurrences of each value and
reconstructs the sorted array from the count table.
Only works for integers (or values mappable to integers).
"""

def counting_sort(arr: list) -> list:
    if not arr:
        return []
    mn, mx = min(arr), max(arr)
    count = [0] * (mx - mn + 1)

    for x in arr:
        count[x - mn] += 1

    return [x + mn for x, c in enumerate(count) for _ in range(c)]


if __name__ == "__main__":
    test = [4, 2, 2, 8, 3, 3, 1]
    print("Input: ", test)
    print("Output:", counting_sort(test))
