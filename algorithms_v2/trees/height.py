"""
Tree Height (Max Depth)
Time:  O(n)
Space: O(h)

Recursively computes the number of nodes along the longest
path from root to a leaf.
"""

from _tree_node import TreeNode, from_list


def height(root) -> int:
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


if __name__ == "__main__":
    tree = from_list([3, 9, 20, None, None, 15, 7])
    print("Height:", height(tree))  # 3

    single = from_list([1])
    print("Height of single node:", height(single))  # 1
