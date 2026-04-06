"""
Lowest Common Ancestor (LCA)
Time:  O(n)
Space: O(h)

The LCA of two nodes p and q is the deepest node that has
both p and q as descendants. If a node itself is p or q,
it counts as its own ancestor.
"""

from _tree_node import TreeNode, from_list


def lca(root, p: int, q: int):
    if not root or root.val == p or root.val == q:
        return root
    left  = lca(root.left,  p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root        # p and q are on opposite sides
    return left or right   # both are in same subtree


if __name__ == "__main__":
    tree = from_list([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    print("LCA(5, 1):", lca(tree, 5, 1).val)  # 3
    print("LCA(5, 4):", lca(tree, 5, 4).val)  # 5
