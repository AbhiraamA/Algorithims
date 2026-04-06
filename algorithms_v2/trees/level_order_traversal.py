"""
Level Order Traversal (BFS)
Time:  O(n)
Space: O(w)  w = max width of tree

Visits nodes level by level using a queue.
Returns a list of lists, one per level.
"""

from collections import deque
from _tree_node import TreeNode, from_list


def level_order(root) -> list:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    tree = from_list([3, 9, 20, None, None, 15, 7])
    print("Level order:")
    for level in level_order(tree):
        print(" ", level)
