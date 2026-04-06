"""
Maximum Subarray — Kadane's Algorithm
Time:  O(n)
Space: O(1)

At each index, decide whether to extend the current subarray
or start fresh. Track the global best along the way.
"""


def max_subarray_sum(nums: list) -> int:
    """Returns the maximum subarray sum."""
    best = cur = nums[0]
    for n in nums[1:]:
        cur  = max(n, cur + n)
        best = max(best, cur)
    return best


def max_subarray(nums: list) -> tuple:
    """Returns (max_sum, start_index, end_index) of the subarray."""
    best_sum  = cur_sum = nums[0]
    best_start = best_end = cur_start = 0

    for i in range(1, len(nums)):
        if nums[i] > cur_sum + nums[i]:
            cur_sum   = nums[i]
            cur_start = i
        else:
            cur_sum += nums[i]

        if cur_sum > best_sum:
            best_sum   = cur_sum
            best_start = cur_start
            best_end   = i

    return best_sum, best_start, best_end


if __name__ == "__main__":
    tests = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],   # [4,-1,2,1] = 6
        [1],                                 # 1
        [-1, -2, -3],                        # -1
        [5, 4, -1, 7, 8],                   # 23
    ]
    for nums in tests:
        s, lo, hi = max_subarray(nums)
        print(f"  {nums}")
        print(f"    max sum = {s}, subarray = {nums[lo:hi+1]}")
