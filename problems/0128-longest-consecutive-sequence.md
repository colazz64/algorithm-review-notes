# 128. Longest Consecutive Sequence

## Link

https://leetcode.cn/problems/longest-consecutive-sequence/

## Tags

HashSet, Array, Sequence

## Status

- Difficulty: Medium
- First solution: Sorting
- Optimized solution: HashSet
- Review status: Need review

## Problem Summary

Given an unsorted array of integers, return the length of the longest consecutive elements sequence.

The key requirement is to solve it in `O(n)` time.

## My First Idea: Sorting

My first solution was to remove duplicates with a map, sort all unique numbers, and then scan the sorted list to count consecutive elements.

This works logically, but the time complexity is `O(n log n)` because of sorting.

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, 1);
        }

        List<Integer> sorted = new ArrayList<>(map.keySet());
        Collections.sort(sorted);

        int maxStreak = 1;
        int currentStreak = 1;

        for (int i = 0; i < sorted.size() - 1; i++) {
            if (sorted.get(i) + 1 == sorted.get(i + 1)) {
                currentStreak++;
            } else {
                currentStreak = 1;
            }

            maxStreak = Math.max(maxStreak, currentStreak);
        }

        return maxStreak;
    }
}
```

## Better Idea: HashSet Start Point Check

The optimized idea is to put all numbers into a `HashSet`.

For each number, only start counting when `num - 1` does not exist.  
That means this number is the beginning of a consecutive sequence.

This avoids repeatedly counting the same sequence.

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        Set<Integer> numSet = new HashSet<>();

        for (int num : nums) {
            numSet.add(num);
        }

        int maxStreak = 0;

        for (int num : numSet) {
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentStreak = 1;

                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                maxStreak = Math.max(maxStreak, currentStreak);
            }
        }

        return maxStreak;
    }
}
```

## Python Solution

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                max_streak = max(max_streak, current_streak)

        return max_streak
```

## Complexity

Sorting solution:

- Time: `O(n log n)`
- Space: `O(n)`

HashSet solution:

- Time: `O(n)`
- Space: `O(n)`

## Mistakes and Notes

- Sorting makes the solution easy to understand, but it does not satisfy the required `O(n)` time.
- The key optimization is not to start counting from every number.
- Only start from `num` when `num - 1` does not exist.
- In Java, use `||` instead of `|` for null checks.

Wrong:

```java
if (nums == null | nums.length == 0)
```

Better:

```java
if (nums == null || nums.length == 0)
```

`||` is short-circuit OR. If `nums == null` is true, Java will not evaluate `nums.length`.