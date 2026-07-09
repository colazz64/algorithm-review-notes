# 283. Move Zeroes

## Link

https://leetcode.cn/problems/move-zeroes/

## Tags

Two Pointers, Array, In-place

## Status

- Difficulty: Easy
- Language: Java, Python
- Review status: Need review

## Problem Summary

Move all zeroes to the end of the array while keeping the relative order of the non-zero elements.

The operation must be done in-place.

## Core Idea

Use two pointers:

- `i` scans every element.
- `j` points to the position where the next non-zero element should be placed.

When `nums[i] != 0`, swap `nums[i]` with `nums[j]`, then move `j` forward.

## Java Solution

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
                j++;
            }
        }
    }
}
```

## Python Solution

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
```

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Mistakes and Notes

This is an in-place problem, so the function should not return a new array.

In Python, the LeetCode signature says:

```python
def moveZeroes(self, nums: List[int]) -> None:
```

That means we modify `nums` directly.

Java needs a temporary variable for swap:

```java
int tmp = nums[i];
nums[i] = nums[j];
nums[j] = tmp;
```

Python can swap directly:

```python
nums[i], nums[j] = nums[j], nums[i]
```

## Pattern

This problem is a classic two-pointer in-place overwrite or swap problem.

The pointer `j` represents the boundary of processed non-zero elements.