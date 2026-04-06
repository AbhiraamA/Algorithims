"""
Reverse a Linked List
Time:  O(n)
Space: O(1)

Iteratively reverses the next pointers of each node.
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

def reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev

if __name__ == "__main__":
    ll = from_list([1, 2, 3, 4, 5])
    print("Original:", ll)
    print("Reversed:", reverse(ll))
