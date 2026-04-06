"""
Add Two Numbers (as Linked Lists)
Time:  O(max(n, m))
Space: O(max(n, m))

Each list stores a number in reverse digit order. Simulates
grade-school addition with a carry value.
e.g. 342 + 465 = 807 → [2,4,3] + [5,6,4] = [7,0,8]
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

def add_two_numbers(l1, l2):
    dummy = Node()
    cur = dummy
    carry = 0
    while l1 or l2 or carry:
        val = carry
        if l1: val += l1.val; l1 = l1.next
        if l2: val += l2.val; l2 = l2.next
        carry, digit = divmod(val, 10)
        cur.next = Node(digit)
        cur = cur.next
    return dummy.next

if __name__ == "__main__":
    l1 = from_list([2, 4, 3])  # 342
    l2 = from_list([5, 6, 4])  # 465
    print("342 + 465 =", add_two_numbers(l1, l2), "→ (807 reversed)")

    l3 = from_list([9, 9, 9])  # 999
    l4 = from_list([1])        # 1
    print("999 +   1 =", add_two_numbers(l3, l4), "→ (1000 reversed)")
