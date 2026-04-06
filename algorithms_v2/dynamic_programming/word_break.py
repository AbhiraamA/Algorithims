"""
Word Break
Time:  O(n²)
Space: O(n)

Determine if a string can be segmented into words from a
given dictionary. dp[i] = True means s[:i] can be segmented.
"""


def word_break(s: str, word_dict: list) -> bool:
    """Returns True if s can be fully segmented using words in word_dict."""
    words = set(word_dict)
    n     = len(s)
    dp    = [False] * (n + 1)
    dp[0] = True  # empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]


def word_break_all(s: str, word_dict: list) -> list:
    """Returns all valid sentence segmentations."""
    words = set(word_dict)
    memo  = {}

    def backtrack(start: int) -> list:
        if start in memo:
            return memo[start]
        if start == len(s):
            return [[]]
        results = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for rest in backtrack(end):
                    results.append([word] + rest)
        memo[start] = results
        return results

    return [" ".join(sentence) for sentence in backtrack(0)]


if __name__ == "__main__":
    print(word_break("leetcode",  ["leet", "code"]))       # True
    print(word_break("applepenapple", ["apple", "pen"]))   # True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False

    print("\nAll segmentations:")
    sentences = word_break_all("catsanddog", ["cat", "cats", "and", "sand", "dog"])
    for s in sentences:
        print(" ", s)
