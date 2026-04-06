"""
Min Heap
Time:  O(log n) push/pop  |  O(1) peek
Space: O(n)

A complete binary tree where every parent is <= its children.
Python's heapq module is a min-heap by default — this wraps it
with a clean class interface.
"""

import heapq


class MinHeap:
    def __init__(self):
        self._data = []

    def push(self, val):
        heapq.heappush(self._data, val)

    def pop(self) -> int:
        return heapq.heappop(self._data)

    def peek(self) -> int:
        return self._data[0]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"MinHeap({sorted(self._data)})"


if __name__ == "__main__":
    h = MinHeap()
    for val in [5, 3, 8, 1, 9, 2]:
        h.push(val)

    print("Heap:", h)
    print("Peek (min):", h.peek())

    print("Pop order:", end=" ")
    while h:
        print(h.pop(), end=" ")
    print()
