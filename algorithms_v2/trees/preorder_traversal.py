"""
Preorder Traversal — Root → Left → Right
Time:  O(n)
Space: O(h)

Used to copy/serialize a tree or evaluate prefix expressions.
"""

from _tree_node import TreeNode, from_list


def preorder_recursive(root) -> list:
    if not root:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def preorder_iterative(root) -> list:
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right: stack.append(node.right)
        if node.left:  stack.append(node.left)
    return result


if __name__ == "__main__":
    tree = from_list([4, 2, 7, 1, 3, 6, 9])
    print("Recursive:", preorder_recursive(tree))
    print("Iterative:", preorder_iterative(tree))
