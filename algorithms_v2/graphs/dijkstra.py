"""
Dijkstra's Shortest Path
Time:  O((V + E) log V)
Space: O(V)

Greedy algorithm using a min-heap. Finds the shortest path
from a source to all other nodes. Requires non-negative weights.
"""

import heapq
from collections import defaultdict


def dijkstra(graph: dict, start: int) -> dict:
    """
    graph[u] = [(v, weight), ...]
    Returns dict of {node: shortest_distance_from_start}.
    """
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    heap = [(0, start)]  # (cost, node)

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return dict(dist)


def dijkstra_path(graph: dict, start: int, end: int) -> list:
    """Returns the actual shortest path from start to end."""
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    prev = {start: None}
    heap = [(0, start)]

    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph.get(node, []):
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(heap, (new_dist, neighbor))

    # Reconstruct path
    path, cur = [], end
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    return path[::-1] if path[0] == start else []


if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    print("Distances from 0:", dijkstra(graph, 0))
    print("Path 0 → 3:      ", dijkstra_path(graph, 0, 3))
