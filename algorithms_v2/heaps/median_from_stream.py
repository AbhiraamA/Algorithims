"""
Find Median from Data Stream
Time:  O(log n) insert  |  O(1) get_median
Space: O(n)

Two heaps: a max-heap for the lower half and a min-heap for
the upper half. We balance them so their sizes differ by at
most 1. The median is always at one of the two heap tops.
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (lower half) — negate values
        self.hi = []  # min-heap (upper half)

    def add_num(self, num: int):
        # Push to max-heap, then balance by moving top to min-heap
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))

        # Keep lo >= hi in size
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self) -> float:
        if len(self.lo) > len(self.hi):
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2.0


if __name__ == "__main__":
    mf = MedianFinder()
    for num in [1, 7, 3, 5, 2]:
        mf.add_num(num)
        print(f"  add {num}  →  median = {mf.find_median()}")
