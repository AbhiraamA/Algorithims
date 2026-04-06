"""
Inorder Traversal — Left → Root → Right
Time:  O(n)
Space: O(h)  h = height of tree

Visits nodes in sorted order for a valid BST.
Implemented both recursively and iteratively.
"""

from _tree_node import TreeNode, from_list


def inorder_recursive(root) -> list:
    if not root:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def inorder_iterative(root) -> list:
    result, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    return result


if __name__ == "__main__":
    tree = from_list([4, 2, 7, 1, 3, 6, 9])
    print("Recursive:", inorder_recursive(tree))
    print("Iterative:", inorder_iterative(tree))
