"""
KMP (Knuth-Morris-Pratt) Pattern Search
Time:  O(n + m)  — n = text length, m = pattern length
Space: O(m)

Preprocesses the pattern into a "longest proper prefix which
is also suffix" (LPS) table to skip redundant comparisons.
"""


def kmp_search(text: str, pattern: str) -> list[int]:
    """Returns all starting indices where pattern occurs in text."""
    if not pattern:
        return []
    lps     = _build_lps(pattern)
    matches = []
    i = j   = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            j = lps[j - 1] if j != 0 else 0
            if j == 0:
                i += 1

    return matches


def _build_lps(pattern: str) -> list[int]:
    """Build the Longest Proper Prefix-Suffix array."""
    lps    = [0] * len(pattern)
    length = 0
    i      = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i]  = length
            i       += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i      += 1

    return lps


if __name__ == "__main__":
    text    = "AABAACAADAABAABA"
    pattern = "AABA"
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at indices: {kmp_search(text, pattern)}")
