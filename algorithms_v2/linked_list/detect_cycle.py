"""
Detect Cycle — Floyd's Tortoise and Hare
Time:  O(n)
Space: O(1)

Two pointers move at different speeds; if they meet, a cycle exists.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val; self.next = next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

if __name__ == "__main__":
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2  # cycle
    print("Has cycle (yes):", has_cycle(n1))

    head = Node(1); head.next = Node(2)
    print("Has cycle (no): ", has_cycle(head))
