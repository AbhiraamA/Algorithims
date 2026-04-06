"""
Union-Find (Disjoint Set Union)
Time:  O(α(n)) per operation — effectively O(1) with optimizations
Space: O(n)

Tracks a collection of disjoint sets. Supports two operations:
  find(x)    — which set does x belong to?
  union(x,y) — merge the sets containing x and y

Optimizations: path compression + union by rank.
Common use: cycle detection, Kruskal's MST, connected components.
"""


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank   = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        """Path compression: flattens the tree on the way up."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns False if already in same set."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(4, 5)
    print("0-1 connected:", uf.connected(0, 1))  # True
    print("0-2 connected:", uf.connected(0, 2))  # False
    uf.union(1, 2)
    print("0-3 connected after union(1,2):", uf.connected(0, 3))  # True
    print("Components:", uf.components)           # 2
