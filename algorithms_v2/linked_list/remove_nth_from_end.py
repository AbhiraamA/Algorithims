"""
Remove Nth Node from End — One Pass
Time:  O(n)
Space: O(1)

Two pointers n+1 apart; when the fast pointer hits None,
slow is sitting just before the node to remove.
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

def remove_nth_from_end(head, n):
    dummy = Node(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next

if __name__ == "__main__":
    print("Original:             ", from_list([1, 2, 3, 4, 5]))
    print("Remove 2nd from end:  ", remove_nth_from_end(from_list([1,2,3,4,5]), 2))
    print("Remove 1st from end:  ", remove_nth_from_end(from_list([1,2,3,4,5]), 1))
