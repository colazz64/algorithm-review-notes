# 1343. Number of Sub-arrays of Size K and Average Greater Than or Equal to Threshold

## Link

https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

## Tags

`Array`, `Sliding Window`

## Problem Summary

Count how many subarrays of size `k` have average greater than or equal to `threshold`.

## Core Idea

Use fixed-size sliding window.

Instead of checking:

```python
window_sum / k >= threshold
```

check:

```python
window_sum >= k * threshold
```

This avoids unnecessary division.

## Java Solution

```java
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
        int sum = 0;
        int target = k * threshold;

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];

            if (i < k - 1) {
                continue;
            }

            if (sum >= target) {
                count++;
            }

            sum -= arr[i - k + 1];
        }

        return count;
    }
}
```

## Python Solution

```python
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        window_sum = 0
        target = k * threshold

        for i in range(len(arr)):
            window_sum += arr[i]

            if i < k - 1:
                continue

            if window_sum >= target:
                count += 1

            window_sum -= arr[i - k + 1]

        return count
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Review Notes

- Same fixed-size sliding window template as 1456 and 643.
- Compare sum with `k * threshold` instead of using average.
