# 643. Maximum Average Subarray I

## Link

https://leetcode.cn/problems/maximum-average-subarray-i/

## Tags

`Array`, `Sliding Window`

## Problem Summary

Find the maximum average value of any contiguous subarray of length `k`.

## Core Idea

Since every valid subarray has the same length `k`, maximizing average is the same as maximizing sum.

## Java Solution

```java
class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            if (i < k - 1) {
                continue;
            }

            max = Math.max(max, sum);
            sum -= nums[i - k + 1];
        }

        return (double) max / k;
    }
}
```

## Python Solution

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            window_sum += nums[i]

            if i < k - 1:
                continue

            max_sum = max(max_sum, window_sum)
            window_sum -= nums[i - k + 1]

        return max_sum / k
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Review Notes

- Use `float('-inf')` when the best value may start very small.
- The window only becomes valid when `i >= k - 1`.
