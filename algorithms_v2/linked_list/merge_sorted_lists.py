"""
Merge Two Sorted Linked Lists
Time:  O(n + m)
Space: O(1)

Uses a dummy head node to simplify edge cases while weaving
two sorted lists together in-place.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next
    def __repr__(self):
        vals, cur = [], self
        while cur: vals.append(str(cur.val)); cur = cur.next
        return " -> ".join(vals)

def from_list(lst):
    if not lst: return None
    head = Node(lst[0]); cur = head
    for v in lst[1:]: cur.next = Node(v); cur = cur.next
    return head

def merge_sorted(l1, l2):
    dummy = Node()
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val: cur.next = l1; l1 = l1.next
        else:                cur.next = l2; l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

if __name__ == "__main__":
    l1 = from_list([1, 3, 5, 7])
    l2 = from_list([2, 4, 6, 8])
    print("L1:    ", l1)
    print("L2:    ", l2)
    print("Merged:", merge_sorted(l1, l2))
