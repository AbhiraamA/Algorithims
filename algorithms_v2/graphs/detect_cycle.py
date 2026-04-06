"""
Detect Cycle — Undirected Graph
Time:  O(V + E)
Space: O(V)

Uses DFS. While traversing, if we reach a node that's already
visited and it's not the parent of the current node, a cycle exists.
"""


def has_cycle(graph: dict, num_nodes: int) -> bool:
    visited = set()

    def dfs(node, parent) -> bool:
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True  # back edge found
        return False

    return any(dfs(n, -1) for n in range(num_nodes) if n not in visited)


if __name__ == "__main__":
    # Graph with cycle: 0-1-2-0
    cyclic = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print("Has cycle (yes):", has_cycle(cyclic, 3))

    # Simple path: 0-1-2
    acyclic = {0: [1], 1: [0, 2], 2: [1]}
    print("Has cycle (no): ", has_cycle(acyclic, 3))
