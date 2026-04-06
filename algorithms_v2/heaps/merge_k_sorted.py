"""
Merge K Sorted Lists
Time:  O(n log k)  — n total elements, k lists
Space: O(k)

Uses a min-heap to always extract the smallest current head
across all k lists, then pushes the next element from that list.
"""

import heapq


def merge_k_sorted(lists: list[list[int]]) -> list:
    result = []
    heap   = []

    # Seed heap with the first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))

    return result


if __name__ == "__main__":
    lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("Input lists:", lists)
    print("Merged:     ", merge_k_sorted(lists))

    lists2 = [[1, 3, 5, 7], [2, 4, 6], [0, 8, 9, 10, 11]]
    print("\nInput lists:", lists2)
    print("Merged:     ", merge_k_sorted(lists2))
