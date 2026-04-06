"""
Find All Anagrams in a String
Time:  O(n)
Space: O(k)  — k = unique chars in p

Sliding window of fixed size len(p). Compares character counts
of the window against the pattern counts at each position.
"""

from collections import Counter


def find_anagrams(s: str, p: str) -> list[int]:
    """Returns starting indices of all anagrams of p in s."""
    if len(p) > len(s):
        return []

    need   = Counter(p)
    window = Counter(s[:len(p)])
    result = [0] if window == need else []

    for i in range(len(p), len(s)):
        # Add new right character
        window[s[i]] += 1

        # Remove leftmost character
        left = s[i - len(p)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]

        if window == need:
            result.append(i - len(p) + 1)

    return result


if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # [0, 6]
    print(find_anagrams("abab", "ab"))          # [0, 1, 2]
