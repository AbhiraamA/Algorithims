"""
Fibonacci — Dynamic Programming
Time:  O(n)
Space: O(1)  — bottom-up iterative

Three approaches shown: naive recursion (exponential), memoization
(top-down), and iterative (bottom-up, space-optimal).
"""

from functools import lru_cache


# Naive recursion — O(2^n) time, included for contrast only
def fib_naive(n: int) -> int:
    if n <= 1: return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# Top-down memoization — O(n) time, O(n) space
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1: return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# Bottom-up iterative — O(n) time, O(1) space
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    for i in [0, 1, 5, 10, 20, 30]:
        print(f"  fib({i:2}) = {fib_dp(i)}")
