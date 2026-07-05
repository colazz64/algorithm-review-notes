# 217. Contains Duplicate

## Link

https://leetcode.cn/problems/contains-duplicate/

## Tags

`Array`, `Set`, `HashSet`

## Problem Summary

Return `true` if any value appears at least twice in the array.  
Return `false` if every value is unique.

## Core Idea

Use a set to store numbers that have appeared before.

When reading a number:

- if it is already in the set, there is a duplicate
- otherwise, add it to the set

## Java Solution

```java
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            if (!set.add(num)) {
                return true;
            }
        }

        return false;
    }
}
```

## Python Solution

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Review Notes

- Java uses `HashSet`.
- Python uses `set`.
- Java `set.add(num)` returns whether the add succeeded.
- Python usually writes the check explicitly with `num in seen`.
