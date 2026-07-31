# 53. Maximum Subarray

## Metadata

| Field | Value |
|---|---|
| Source | LeetCode Hot 100 |
| Topics | Dynamic Programming, Array, Kadane Algorithm |
| Difficulty | Medium |
| Status | Done |
| Review Priority | High |

## Links

- LeetCode: https://leetcode.cn/problems/maximum-subarray/
- Collection: [LeetCode Hot 100](../leetcode-hot100/README.md)
- Topic: [Dynamic Programming](../topics/dynamic-programming.md)
- Topic: [Array](../topics/array.md)

## Problem Summary

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

A subarray must be continuous.

## Core Idea

Use Kadane's Algorithm.

For each position `i`, think about one question:

Should I continue the previous subarray, or start a new subarray from `nums[i]`?

So we define:

```text
currentSum = maximum subarray sum ending at current index
maxSum = maximum subarray sum found so far
```

Transition:

```text
currentSum = max(currentSum + nums[i], nums[i])
maxSum = max(maxSum, currentSum)
```

Meaning:

- `currentSum + nums[i]`: continue the previous subarray
- `nums[i]`: start a new subarray from current position

## Java Solution

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int currentSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; i++) {
            currentSum = Math.max(currentSum + nums[i], nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }

        return maxSum;
    }
}
```

## Python Solution

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
```

## Complexity

| Type | Complexity |
|---|---|
| Time | `O(n)` |
| Space | `O(1)` |

## Step-by-step Logic

Example:

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

When we reach `4`, the previous sum is bad, so we start over from `4`.

Then:

```text
4 + (-1) + 2 + 1 = 6
```

The maximum subarray is:

```text
[4, -1, 2, 1]
```

Answer:

```text
6
```

## Mistakes and Notes

### Why initialize with `nums[0]`?

Do not initialize `maxSum` as `0`.

Wrong:

```java
int maxSum = 0;
```

If all numbers are negative, this will incorrectly return `0`.

Example:

```text
nums = [-3, -2, -5]
```

Correct answer should be:

```text
-2
```

So initialize both values with the first element:

```java
int currentSum = nums[0];
int maxSum = nums[0];
```

### What does `currentSum` mean?

`currentSum` is not the global answer.

It only means:

```text
the best subarray sum ending at current index
```

`maxSum` is the final answer.

## Pattern

This is a classic one-dimensional dynamic programming problem.

DP definition:

```text
dp[i] = maximum subarray sum ending at index i
```

Transition:

```text
dp[i] = max(dp[i - 1] + nums[i], nums[i])
```

Because we only need the previous state, we can compress the DP array into one variable:

```text
currentSum
```

## Review Notes

- This is not a sliding window problem.
- Negative numbers make normal sliding window unreliable.
- The key is deciding whether to continue the previous subarray or restart at the current number.
- Initialize with `nums[0]`, not `0`.