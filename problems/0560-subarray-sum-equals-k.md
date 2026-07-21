# 560. Subarray Sum Equals K

## Metadata

| Field | Value |
|---|---|
| Source | LeetCode Hot 100 |
| Topics | Prefix Sum, HashMap, Array |
| Difficulty | Medium |
| Status | Done |
| Review Priority | High |

## Links

- LeetCode: https://leetcode.cn/problems/subarray-sum-equals-k/
- Collection: [LeetCode Hot 100](../leetcode-hot100/README.md)
- Topic: [Prefix Sum](../topics/prefix-sum.md)
- Topic: [HashMap](../topics/hash-map.md)

## Problem Summary

Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

A subarray must be continuous.

## Core Idea

Use prefix sum and HashMap.

Let:

```text
currentSum = nums[0] + nums[1] + ... + nums[i]
```

If a previous prefix sum is:

```text
target = currentSum - k
```

then the subarray between that previous prefix position and current position has sum `k`.

So every time we reach a new `currentSum`, we check how many times `currentSum - k` appeared before.

## Why Put `0 -> 1` First?

We initialize the map with:

```java
map.put(0, 1);
```

This handles the case where a subarray starting from index `0` has sum `k`.

Example:

```text
nums = [1, 2, 3], k = 3
```

When `currentSum = 3`, we need:

```text
target = currentSum - k = 3 - 3 = 0
```

So the initial `0 -> 1` means there is one prefix sum before the array starts.

## Java Solution

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        int currentSum = 0;
        int count = 0;

        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);

        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];

            int target = currentSum - k;

            if (map.containsKey(target)) {
                count += map.get(target);
            }

            map.put(currentSum, map.getOrDefault(currentSum, 0) + 1);
        }

        return count;
    }
}
```

## Python Solution

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0

        prefix_count = {0: 1}

        for num in nums:
            current_sum += num

            target = current_sum - k

            if target in prefix_count:
                count += prefix_count[target]

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return count
```

## Complexity

| Type | Complexity |
|---|---|
| Time | `O(n)` |
| Space | `O(n)` |

## Mistakes and Notes

### Why not use sliding window?

This problem can contain negative numbers.

When negative numbers exist, expanding the window does not always increase the sum, and shrinking the window does not always decrease the sum.

So the normal sliding window idea does not work reliably.

Prefix sum with HashMap is safer.

### Key Formula

```text
currentSum - previousSum = k
```

So:

```text
previousSum = currentSum - k
```

That is why we check:

```java
int target = currentSum - k;
```

## Pattern

This is a classic prefix sum + HashMap counting problem.

Template:

```python
prefix_count = {0: 1}
current_sum = 0
answer = 0

for num in nums:
    current_sum += num
    answer += prefix_count.get(current_sum - k, 0)
    prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
```

## Review Notes

- `map` stores how many times each prefix sum appeared.
- `count += map.get(target)` means there may be multiple previous prefix sums that can form valid subarrays.
- `map.put(0, 1)` is important for subarrays starting at index `0`.