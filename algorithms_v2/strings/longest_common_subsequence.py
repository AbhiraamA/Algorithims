"""
Longest Common Subsequence (LCS)
Time:  O(m * n)
Space: O(m * n)

Finds the longest sequence of characters that appears in both
strings in the same order (not necessarily contiguous).
e.g. LCS("ABCBDAB", "BDCAB") = "BCAB" or "BDAB" (length 4)
"""


def lcs_length(s1: str, s2: str) -> int:
    """Returns just the length of the LCS."""
    m, n = len(s1), len(s2)
    dp   = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def lcs_string(s1: str, s2: str) -> str:
    """Returns one actual LCS string via backtracking."""
    m, n = len(s1), len(s2)
    dp   = [[""] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]


if __name__ == "__main__":
    s1, s2 = "ABCBDAB", "BDCAB"
    print(f"s1: {s1}")
    print(f"s2: {s2}")
    print(f"LCS length: {lcs_length(s1, s2)}")
    print(f"LCS string: {lcs_string(s1, s2)}")
