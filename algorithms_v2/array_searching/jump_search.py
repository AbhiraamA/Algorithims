"""
Jump Search
Time:  O(√n)
Space: O(1)
Requires: sorted array

Jumps ahead by √n steps until an element >= target is found,
then does a linear scan backwards. Sits between linear and
binary search — useful when jumping backwards is costly.
"""

import math


def jump_search(arr: list, target) -> int:
    """Returns index of target or -1."""
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    print("Array:", arr)
    print("Search 55:", jump_search(arr, 55))
    print("Search 10:", jump_search(arr, 10))
