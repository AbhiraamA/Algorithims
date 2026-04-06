"""
Edit Distance (Levenshtein Distance)
Time:  O(m * n)
Space: O(n)  — space-optimized with rolling array

Minimum number of single-character edits (insert, delete,
replace) required to transform s1 into s2.
"""


def edit_distance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    # dp[j] = edit distance between s1[:i] and s2[:j]
    dp = list(range(n + 1))

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if s1[i - 1] == s2[j - 1]:
                dp[j] = prev                          # no edit needed
            else:
                dp[j] = 1 + min(prev,                 # replace
                                dp[j],                # delete
                                dp[j - 1])            # insert
            prev = temp

    return dp[n]


if __name__ == "__main__":
    pairs = [
        ("kitten", "sitting"),   # 3
        ("sunday", "saturday"),  # 3
        ("",       "abc"),       # 3
        ("abc",    "abc"),       # 0
        ("horse",  "ros"),       # 3
    ]
    for s1, s2 in pairs:
        print(f"  {s1!r:10} → {s2!r:10}  distance = {edit_distance(s1, s2)}")
