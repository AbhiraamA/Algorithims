"""
Breadth-First Search (BFS)
Time:  O(V + E)
Space: O(V)

Explores all neighbors at the current depth before going deeper.
Finds shortest path (in hops) in unweighted graphs.
"""

from collections import deque


def bfs(graph: dict, start: int) -> list:
    """Returns nodes in BFS visit order."""
    visited = {start}
    queue   = deque([start])
    order   = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def shortest_path(graph: dict, start: int, end: int) -> list:
    """Returns shortest path (by hops) from start to end, or []."""
    visited = {start: None}
    queue   = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = visited[node]
            return path[::-1]
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)
    return []


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [5], 5: []}
    print("BFS order:      ", bfs(graph, 0))
    print("Shortest 0 → 5:", shortest_path(graph, 0, 5))
