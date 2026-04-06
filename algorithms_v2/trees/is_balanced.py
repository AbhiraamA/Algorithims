"""
Check if Binary Tree is Height-Balanced
Time:  O(n)
Space: O(h)

A tree is balanced if, for every node, the heights of its
left and right subtrees differ by at most 1.
Uses a single post-order pass — returns -1 to signal imbalance.
"""

from _tree_node import TreeNode, from_list


def is_balanced(root) -> bool:
    def check(node) -> int:
        if not node:
            return 0
        left  = check(node.left)
        right = check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


if __name__ == "__main__":
    balanced   = from_list([3, 9, 20, None, None, 15, 7])
    unbalanced = from_list([1, 2, 2, 3, 3, None, None, 4, 4])
    print("Balanced:  ", is_balanced(balanced))    # True
    print("Unbalanced:", is_balanced(unbalanced))  # False
