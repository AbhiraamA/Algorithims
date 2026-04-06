"""
Check if Linked List is a Palindrome
Time:  O(n)
Space: O(1)

Finds the middle, reverses the second half, compares both
halves node by node, then restores the list.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def from_list(lst):
    if not lst: return None
    head = Node(lst[0]); cur = head
    for v in lst[1:]: cur.next = Node(v); cur = cur.next
    return head

def _find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    return slow

def _reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next; cur.next = prev; prev = cur; cur = nxt
    return prev

def is_palindrome(head):
    mid = _find_middle(head)
    second = _reverse(mid)
    p1, p2, result = head, second, True
    while p2:
        if p1.val != p2.val: result = False; break
        p1 = p1.next; p2 = p2.next
    _reverse(second)  # restore original structure
    return result

if __name__ == "__main__":
    print("[1,2,3,2,1] palindrome:", is_palindrome(from_list([1,2,3,2,1])))
    print("[1,2,2,1]   palindrome:", is_palindrome(from_list([1,2,2,1])))
    print("[1,2,3,4,5] palindrome:", is_palindrome(from_list([1,2,3,4,5])))
