"""
Number of Islands
Time:  O(m * n)
Space: O(m * n)  — recursion stack in worst case

Classic graph problem on a 2D grid. Each '1' is land, '0' is water.
Uses DFS to "sink" each island (mark visited cells) as it's counted.
"""


def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def sink(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark visited
        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                sink(r, c)
                count += 1

    return count


if __name__ == "__main__":
    grid1 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]
    print("Islands (expect 3):", num_islands(grid1))

    grid2 = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"],
    ]
    print("Islands (expect 1):", num_islands(grid2))
