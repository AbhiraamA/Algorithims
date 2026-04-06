"""
Matrix Chain Multiplication
Time:  O(n³)
Space: O(n²)

Finds the optimal order to multiply a chain of matrices to
minimize total scalar multiplications.

dims[i] and dims[i+1] define the dimensions of matrix i.
e.g. dims = [10, 30, 5, 60] → matrices A(10×30), B(30×5), C(5×60)
"""


def matrix_chain(dims: list) -> int:
    """Returns the minimum number of scalar multiplications."""
    n  = len(dims) - 1   # number of matrices
    dp = [[0] * n for _ in range(n)]

    # length = number of matrices in the chain being considered
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j      = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = (dp[i][k]
                        + dp[k + 1][j]
                        + dims[i] * dims[k + 1] * dims[j + 1])
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


def matrix_chain_order(dims: list) -> tuple:
    """Returns (min_cost, optimal_parenthesization string)."""
    n    = len(dims) - 1
    dp   = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j        = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = (dp[i][k]
                        + dp[k + 1][j]
                        + dims[i] * dims[k + 1] * dims[j + 1])
                if cost < dp[i][j]:
                    dp[i][j]    = cost
                    split[i][j] = k

    def build_string(i, j):
        if i == j:
            return f"M{i + 1}"
        k = split[i][j]
        return f"({build_string(i, k)} × {build_string(k + 1, j)})"

    return dp[0][n - 1], build_string(0, n - 1)


if __name__ == "__main__":
    dims = [10, 30, 5, 60]
    cost, order = matrix_chain_order(dims)
    print(f"Dims: {dims}")
    print(f"Min multiplications: {cost}")
    print(f"Optimal order: {order}")

    dims2 = [40, 20, 30, 10, 30]
    cost2, order2 = matrix_chain_order(dims2)
    print(f"\nDims: {dims2}")
    print(f"Min multiplications: {cost2}")
    print(f"Optimal order: {order2}")
