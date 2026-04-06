"""
Validate Binary Search Tree
Time:  O(n)
Space: O(h)

Every node must satisfy: all left descendants < node < all right
descendants. Tracks valid (lo, hi) range as we recurse down.
"""

from _tree_node import TreeNode, from_list


def is_valid_bst(root) -> bool:
    def validate(node, lo=float('-inf'), hi=float('inf')) -> bool:
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return (validate(node.left,  lo, node.val) and
                validate(node.right, node.val, hi))

    return validate(root)


if __name__ == "__main__":
    valid   = from_list([2, 1, 3])
    invalid = from_list([5, 1, 4, None, None, 3, 6])
    print("Valid BST:  ", is_valid_bst(valid))    # True
    print("Invalid BST:", is_valid_bst(invalid))  # False
