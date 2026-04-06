"""
Bellman-Ford Shortest Path
Time:  O(V * E)
Space: O(V)

Relaxes all edges V-1 times. Handles negative edge weights
and detects negative cycles (unlike Dijkstra).
"""


def bellman_ford(edges: list, num_nodes: int, start: int) -> dict | None:
    """
    edges = [(u, v, weight), ...]
    Returns dict of shortest distances, or None if negative cycle detected.
    """
    dist = {i: float('inf') for i in range(num_nodes)}
    dist[start] = 0

    # Relax all edges V-1 times
    for _ in range(num_nodes - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # negative cycle exists

    return dist


if __name__ == "__main__":
    # Standard case
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    print("Distances:", bellman_ford(edges, 4, 0))

    # Negative cycle
    neg_edges = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
    result = bellman_ford(neg_edges, 3, 0)
    print("Negative cycle detected:", result is None)
