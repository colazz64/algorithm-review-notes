# 1. Two Sum

## Link

https://leetcode.cn/problems/two-sum/

## Tags

`Array`, `HashMap`

## Problem Summary

Given an array and a target, return the indices of two numbers that add up to the target.

## Brute Force Idea

Try every pair.

## Java Brute Force

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int left = nums[i];

            for (int j = i + 1; j < n; j++) {
                int right = nums[j];

                if (left + right == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[0];
    }
}
```

## Optimized Idea

For each number, check whether `target - nums[i]` appeared before.

## Python Solution

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in seen:
                return [seen[need], i]

            seen[num] = i

        return []
```

## Complexity

- Brute force time: `O(n^2)`
- Optimized time: `O(n)`
- Optimized space: `O(n)`

## Review Notes

- This is the classic HashMap complement pattern.
- Store value -> index.
- Check before insert to avoid using the same element twice.
