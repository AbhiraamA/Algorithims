"""
Radix Sort
Time:  O(d * n)  — d = number of digits
Space: O(n + k)
Stable: Yes

Non-comparison sort. Sorts integers digit by digit from least
significant to most significant using counting sort as a
subroutine. Excellent for large arrays of integers.
"""

def radix_sort(arr: list) -> list:
    if not arr:
        return []
    arr = arr[:]
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr


def _counting_sort_by_digit(arr: list, exp: int) -> list:
    n = len(arr)
    output = [0] * n
    count  = [0] * 10

    for x in arr:
        count[(x // exp) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        idx = (arr[i] // exp) % 10
        output[count[idx] - 1] = arr[i]
        count[idx] -= 1

    return output


if __name__ == "__main__":
    test = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Input: ", test)
    print("Output:", radix_sort(test))
