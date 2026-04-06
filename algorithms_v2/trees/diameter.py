"""
Diameter of a Binary Tree
Time:  O(n)
Space: O(h)

The diameter is the length of the longest path between any
two nodes (measured in edges). The path may or may not pass
through the root.
"""

from _tree_node import TreeNode, from_list


def diameter(root) -> int:
    best = [0]

    def depth(node) -> int:
        if not node:
            return 0
        l = depth(node.left)
        r = depth(node.right)
        best[0] = max(best[0], l + r)
        return 1 + max(l, r)

    depth(root)
    return best[0]


if __name__ == "__main__":
    tree = from_list([1, 2, 3, 4, 5])
    print("Diameter:", diameter(tree))  # 3  (path: 4-2-1-3 or 5-2-1-3)
