# 303. Range Sum Query Immutable

## Metadata

| Field | Value |
|---|---|
| Source | Prefix Sum Practice |
| Topics | Prefix Sum, Array, Design |
| Difficulty | Easy |
| Status | Done |
| Review Priority | Medium |

## Links

- LeetCode: https://leetcode.cn/problems/range-sum-query-immutable/
- Topic: [Prefix Sum](../topics/prefix-sum.md)

## Problem Summary

Given an integer array `nums`, design a class that can answer multiple range sum queries.

Each query asks for:

```text
sumRange(left, right)
```

which returns the sum of elements from index `left` to index `right`.

## Core Idea

Use prefix sum.

Create an array `preSum` where:

```text
preSum[i + 1] = preSum[i] + nums[i]
```

So:

```text
preSum[0] = 0
preSum[1] = nums[0]
preSum[2] = nums[0] + nums[1]
```

Then the sum from `left` to `right` is:

```text
preSum[right + 1] - preSum[left]
```

## Why `nums.length + 1`?

We create `preSum` with one extra space:

```java
preSum = new int[nums.length + 1];
```

This makes range calculation cleaner.

The empty prefix before index `0` is stored as:

```text
preSum[0] = 0
```

Then every range can use the same formula:

```text
preSum[right + 1] - preSum[left]
```

## Java Solution

```java
class NumArray {

    private int[] preSum;

    public NumArray(int[] nums) {
        preSum = new int[nums.length + 1];

        for (int i = 0; i < nums.length; i++) {
            preSum[i + 1] = preSum[i] + nums[i];
        }
    }

    public int sumRange(int left, int right) {
        return preSum[right + 1] - preSum[left];
    }
}
```

## Python Solution

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.pre_sum[i + 1] = self.pre_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]
```

## Complexity

| Operation | Complexity |
|---|---|
| Constructor | `O(n)` |
| `sumRange` | `O(1)` |
| Space | `O(n)` |

## Mistakes and Notes

### Prefix Sum Index Shift

The hardest part is understanding the index shift.

```text
nums:   nums[0] nums[1] nums[2]
preSum: 0      sum0    sum0+1  sum0+1+2
```

So `preSum[i]` means the sum of elements before index `i`.

That is why:

```text
sumRange(left, right) = preSum[right + 1] - preSum[left]
```

## Pattern

This is the basic prefix sum template.

```python
pre_sum = [0] * (len(nums) + 1)

for i in range(len(nums)):
    pre_sum[i + 1] = pre_sum[i] + nums[i]
```

Query:

```python
range_sum = pre_sum[right + 1] - pre_sum[left]
```

## Review Notes

- Use `n + 1` length to simplify range queries.
- `preSum[0] = 0` represents the empty prefix.
- This is useful when there are many repeated range sum queries.