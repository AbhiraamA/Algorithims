"""
Postorder Traversal — Left → Right → Root
Time:  O(n)
Space: O(h)

Used to delete a tree, evaluate postfix expressions, or
compute directory sizes (children before parent).
"""

from _tree_node import TreeNode, from_list


def postorder_recursive(root) -> list:
    if not root:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def postorder_iterative(root) -> list:
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:  stack.append(node.left)
        if node.right: stack.append(node.right)
    return result[::-1]


if __name__ == "__main__":
    tree = from_list([4, 2, 7, 1, 3, 6, 9])
    print("Recursive:", postorder_recursive(tree))
    print("Iterative:", postorder_iterative(tree))
