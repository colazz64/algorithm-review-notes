# 11. Container With Most Water

## Metadata

| Field | Value |
|---|---|
| Source | LeetCode Hot 100, NeetCode 150 |
| Topics | Two Pointers, Array, Greedy |
| Difficulty | Medium |
| Status | Done |
| Review Priority | Medium |

## Links

- LeetCode: https://leetcode.cn/problems/container-with-most-water/
- Collection: [LeetCode Hot 100](../leetcode-hot100/README.md)
- Collection: [NeetCode 150](../neetcode150/README.md)
- Topic: [Two Pointers](../topics/two-pointers.md)

## Problem Summary

Given an integer array `height`, where each element represents a vertical line, choose two lines that together with the x-axis can contain the most water.

The area is calculated as:

```text
area = width * min(height[left], height[right])
```

The goal is to find the maximum possible area.

## Core Idea

Use two pointers:

- `left` starts from the beginning.
- `right` starts from the end.
- Each time, calculate the area between `left` and `right`.
- Move the pointer with the smaller height.

The important logic is:

The amount of water is limited by the shorter wall.  
If we move the taller wall, the width becomes smaller, but the shorter wall stays the same, so the area cannot become better.  
Only moving the shorter wall gives us a chance to find a taller boundary and possibly increase the area.

## Java Solution

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int width = right - left;
            int depth = Math.min(height[left], height[right]);
            int area = width * depth;

            maxArea = Math.max(maxArea, area);

            if (height[left] <= height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
```

## Python Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            depth = min(height[left], height[right])
            area = width * depth

            max_area = max(max_area, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

## Complexity

| Type | Complexity |
|---|---|
| Time | `O(n)` |
| Space | `O(1)` |

## Mistakes and Notes

### Why move the shorter side?

For the current pair:

```text
area = (right - left) * min(height[left], height[right])
```

When we move either pointer, the width must decrease.

If we move the taller side, the shorter side is still the bottleneck, and the width becomes smaller, so the area cannot improve.

If we move the shorter side, there is at least a chance to find a taller wall and increase the minimum height.

So the rule is:

```text
Move the shorter wall.
```

## Pattern

This is a classic opposite-direction two pointers problem.

Template:

```python
left = 0
right = len(nums) - 1

while left < right:
    # calculate answer

    if should_move_left:
        left += 1
    else:
        right -= 1
```

## Review Notes

- This problem is not solved by checking every pair.
- Brute force is `O(n^2)`.
- The two-pointer method works because the width always decreases, so the only useful move is to try to improve the shorter boundary.