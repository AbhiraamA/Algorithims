"""
Kth Largest Element
Time:  O(n log k)
Space: O(k)

Maintains a min-heap of size k. After processing all elements,
the root of the heap is the kth largest value seen.
"""

import heapq


def kth_largest(nums: list, k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def k_largest_elements(nums: list, k: int) -> list:
    """Returns the k largest elements (sorted descending)."""
    return heapq.nlargest(k, nums)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    print("Array:", nums)
    print("2nd largest:      ", kth_largest(nums, 2))   # 5
    print("3 largest values: ", k_largest_elements(nums, 3))  # [6, 5, 4]

    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print("\nArray:", nums2)
    print("4th largest:", kth_largest(nums2, 4))  # 4
