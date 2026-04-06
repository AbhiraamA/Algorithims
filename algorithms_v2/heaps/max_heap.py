"""
Max Heap
Time:  O(log n) push/pop  |  O(1) peek
Space: O(n)

Simulated using Python's min-heap by negating all values.
Every parent is >= its children.
"""

import heapq


class MaxHeap:
    def __init__(self):
        self._data = []

    def push(self, val):
        heapq.heappush(self._data, -val)

    def pop(self) -> int:
        return -heapq.heappop(self._data)

    def peek(self) -> int:
        return -self._data[0]

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"MaxHeap({sorted([-x for x in self._data], reverse=True)})"


if __name__ == "__main__":
    h = MaxHeap()
    for val in [5, 3, 8, 1, 9, 2]:
        h.push(val)

    print("Heap:", h)
    print("Peek (max):", h.peek())

    print("Pop order:", end=" ")
    while h:
        print(h.pop(), end=" ")
    print()
