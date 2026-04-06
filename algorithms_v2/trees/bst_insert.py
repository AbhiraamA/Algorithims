"""
BST Insert
Time:  O(h)  — O(log n) avg, O(n) worst (skewed tree)
Space: O(h)

Recursively walks left or right based on the value,
inserting a new leaf at the correct position.
"""

from _tree_node import TreeNode, from_list


def bst_insert(root, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left  = bst_insert(root.left,  val)
    else:
        root.right = bst_insert(root.right, val)
    return root


if __name__ == "__main__":
    from level_order_traversal import level_order
    tree = from_list([4, 2, 7, 1, 3])
    print("Before:", level_order(tree))
    tree = bst_insert(tree, 5)
    print("After inserting 5:", level_order(tree))
