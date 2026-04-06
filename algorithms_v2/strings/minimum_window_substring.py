"""
Minimum Window Substring
Time:  O(n)
Space: O(k)  — k = unique chars in t

Sliding window. Expands the right pointer until all characters
in t are covered, then shrinks from the left to find the minimum.
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need    = Counter(t)
    missing = len(t)   # total characters still needed
    best    = ""
    lo      = 0

    for hi, char in enumerate(s):
        if need[char] > 0:
            missing -= 1
        need[char] -= 1

        if missing == 0:
            # Shrink from the left
            while need[s[lo]] < 0:
                need[s[lo]] += 1
                lo += 1

            window = s[lo:hi + 1]
            if not best or len(window) < len(best):
                best = window

            # Slide window forward
            need[s[lo]] += 1
            missing += 1
            lo += 1

    return best


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    print(min_window("a", "a"))                # "a"
    print(min_window("a", "aa"))               # ""
