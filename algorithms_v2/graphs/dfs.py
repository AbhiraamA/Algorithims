"""
Depth-First Search (DFS)
Time:  O(V + E)
Space: O(V)

Explores as far as possible along each branch before backtracking.
Used for cycle detection, topological sort, connected components.
"""


def dfs_iterative(graph: dict, start: int) -> list:
    visited = set()
    stack   = [start]
    order   = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return order


def dfs_recursive(graph: dict, start: int, visited: set = None) -> list:
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs_recursive(graph, neighbor, visited))
    return order


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
    print("DFS iterative:", dfs_iterative(graph, 0))
    print("DFS recursive:", dfs_recursive(graph, 0))
