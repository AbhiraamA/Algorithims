"""
Longest Palindromic Substring
Time:  O(n²)
Space: O(1)

Expand-around-center approach. For each character (and each
pair of adjacent characters), expands outward as long as
the characters match.
"""


def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    def expand(l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    best = ""
    for i in range(len(s)):
        odd  = expand(i, i)      # odd-length palindromes
        even = expand(i, i + 1)  # even-length palindromes
        if len(odd)  > len(best): best = odd
        if len(even) > len(best): best = even

    return best


if __name__ == "__main__":
    tests = ["babad", "cbbd", "racecar", "abcba", "a", "ac"]
    for s in tests:
        print(f"  {s!r:12}  →  {longest_palindrome(s)!r}")
