"""
Find Middle Node
Time:  O(n)
Space: O(1)

Fast pointer moves 2x speed of slow; when fast reaches end,
slow is at the middle.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def from_list(lst):
    if not lst: return None
    head = Node(lst[0]); cur = head
    for v in lst[1:]: cur.next = Node(v); cur = cur.next
    return head

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    print("Middle of [1,2,3,4,5]:", find_middle(from_list([1,2,3,4,5])).val)
    print("Middle of [1,2,3,4]:  ", find_middle(from_list([1,2,3,4])).val)
