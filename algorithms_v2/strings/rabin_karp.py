"""
Rabin-Karp Pattern Search
Time:  O(n + m) avg  |  O(nm) worst (hash collisions)
Space: O(1)

Uses a rolling hash to compare pattern against substrings in O(1).
When hashes match, verifies with a direct string comparison to
handle collisions.
"""


def rabin_karp(text: str, pattern: str) -> list[int]:
    """Returns all starting indices where pattern occurs in text."""
    n, m   = len(text), len(pattern)
    base   = 256
    mod    = 101
    if m > n:
        return []

    h      = pow(base, m - 1, mod)
    p_hash = 0
    t_hash = 0
    matches = []

    # Compute initial hashes
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % mod
        t_hash = (base * t_hash + ord(text[i]))    % mod

    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            matches.append(i)
        if i < n - m:
            # Roll the hash forward
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if t_hash < 0:
                t_hash += mod

    return matches


if __name__ == "__main__":
    text    = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    print(f"Text:    {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at indices: {rabin_karp(text, pattern)}")
