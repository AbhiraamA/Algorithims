"""
BST Delete
Time:  O(h)  — O(log n) avg, O(n) worst
Space: O(h)

Three cases:
  1. Node has no children   → just remove it
  2. Node has one child     → replace with that child
  3. Node has two children  → replace with in-order successor
     (smallest node in right subtree), then delete the successor
"""

from _tree_node import TreeNode, from_list


def bst_delete(root, key: int) -> TreeNode:
    if not root:
        return None
    if key < root.val:
        root.left  = bst_delete(root.left,  key)
    elif key > root.val:
        root.right = bst_delete(root.right, key)
    else:
        if not root.left:  return root.right
        if not root.right: return root.left
        # Find in-order successor (min of right subtree)
        successor = root.right
        while successor.left:
            successor = successor.left
        root.val   = successor.val
        root.right = bst_delete(root.right, successor.val)
    return root


if __name__ == "__main__":
    from level_order_traversal import level_order
    tree = from_list([5, 3, 7, 2, 4, 6, 8])
    print("Before:          ", level_order(tree))
    tree = bst_delete(tree, 3)
    print("After deleting 3:", level_order(tree))
