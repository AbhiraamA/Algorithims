"""
Merge Sort
Time:  O(n log n) — all cases
Space: O(n)
Stable: Yes

Divide-and-conquer: splits array in half, recursively sorts
each half, then merges the two sorted halves. Preferred when
stability matters or for linked lists.
"""

def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]


if __name__ == "__main__":
    test = [38, 27, 43, 3, 9, 82, 10]
    print("Input: ", test)
    print("Output:", merge_sort(test))
