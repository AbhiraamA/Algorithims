"""
Topological Sort — Kahn's Algorithm (BFS)
Time:  O(V + E)
Space: O(V)

Orders nodes of a DAG so every directed edge u → v has u
appearing before v. Returns empty list if a cycle is detected.

Common use: task scheduling, build systems, course prerequisites.
"""

from collections import deque


def topological_sort(graph: dict, num_nodes: int) -> list:
    """
    graph[u] = [v, ...] (directed edges u → v)
    Returns topological ordering, or [] if cycle exists.
    """
    in_degree = [0] * num_nodes
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Start with all nodes that have no incoming edges
    queue = deque(n for n in range(num_nodes) if in_degree[n] == 0)
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_nodes else []  # empty = cycle


def topological_sort_dfs(graph: dict, num_nodes: int) -> list:
    """DFS-based variant using a visited stack."""
    visited = set()
    stack   = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for n in range(num_nodes):
        if n not in visited:
            dfs(n)

    return stack[::-1]


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: [], 5: []}
    print("Kahn's BFS:", topological_sort(graph, 6))
    print("DFS-based: ", topological_sort_dfs(graph, 6))
