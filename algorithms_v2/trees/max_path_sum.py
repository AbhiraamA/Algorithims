"""
Maximum Path Sum
Time:  O(n)
Space: O(h)

A path is any sequence of nodes with no repeated nodes.
At each node, we track the best "split" (going both left and
right through the node) vs the best single-branch gain.
"""

from _tree_node import TreeNode, from_list


def max_path_sum(root) -> int:
    best = [float('-inf')]

    def gain(node) -> int:
        if not node:
            return 0
        l = max(gain(node.left),  0)
        r = max(gain(node.right), 0)
        best[0] = max(best[0], node.val + l + r)
        return node.val + max(l, r)

    gain(root)
    return best[0]


if __name__ == "__main__":
    tree1 = from_list([1, 2, 3])
    print("Max path sum [1,2,3]:      ", max_path_sum(tree1))  # 6

    tree2 = from_list([-10, 9, 20, None, None, 15, 7])
    print("Max path sum [-10,9,20..]: ", max_path_sum(tree2))  # 42
