# 239. Sliding Window Maximum

## Metadata

| Field | Value |
|---|---|
| Source | LeetCode Hot 100 |
| Topics | Sliding Window, Monotonic Queue, Deque |
| Difficulty | Hard |
| Status | Done |
| Review Priority | High |

## Links

- LeetCode: https://leetcode.cn/problems/sliding-window-maximum/
- Collection: [LeetCode Hot 100](../leetcode-hot100/README.md)
- Topic: [Sliding Window](../topics/sliding-window.md)
- Topic: [Monotonic Queue](../topics/monotonic-queue.md)

## Problem Summary

Given an integer array `nums` and an integer `k`, return the maximum value in every sliding window of size `k`.

For each window, we need to find the maximum number efficiently.

## Core Idea

Use a monotonic decreasing deque.

The deque stores **indices**, not values.

Why store indices?

Because we need to know whether the element is outside the current window.

The deque keeps indices whose values are in decreasing order:

```text
nums[deque[0]] >= nums[deque[1]] >= nums[deque[2]]
```

So the front of the deque always points to the maximum value of the current window.

## Java Solution

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];
        Deque<Integer> deque = new ArrayDeque<>();

        int index = 0;

        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];

            // 1. Maintain decreasing deque
            while (!deque.isEmpty() && nums[deque.peekLast()] <= current) {
                deque.pollLast();
            }

            // 2. Add current index
            deque.offerLast(i);

            // 3. Remove indices outside the current window
            int left = i - k + 1;

            while (!deque.isEmpty() && deque.peekFirst() < left) {
                deque.pollFirst();
            }

            // 4. Record answer after the first full window is formed
            if (i >= k - 1) {
                ans[index++] = nums[deque.peekFirst()];
            }
        }

        return ans;
    }
}
```

## Python Solution

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i, num in enumerate(nums):
            # 1. Maintain decreasing deque
            while q and nums[q[-1]] <= num:
                q.pop()

            # 2. Add current index
            q.append(i)

            # 3. Remove indices outside the current window
            left = i - k + 1

            if q[0] < left:
                q.popleft()

            # 4. Record answer after the window is formed
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans
```

## Complexity

| Type | Complexity |
|---|---|
| Time | `O(n)` |
| Space | `O(k)` |

Each index enters the deque once and leaves the deque once, so the total time complexity is `O(n)`.

## Step-by-step Logic

For each index `i`:

### 1. Remove smaller elements from the back

```java
while (!deque.isEmpty() && nums[deque.peekLast()] <= current) {
    deque.pollLast();
}
```

If the current value is larger than or equal to the value at the back of the deque, the old value can never become the maximum again.

So we remove it.

### 2. Add current index

```java
deque.offerLast(i);
```

The deque stores indices.

### 3. Remove elements outside the window

```java
int left = i - k + 1;

while (!deque.isEmpty() && deque.peekFirst() < left) {
    deque.pollFirst();
}
```

If the index at the front is smaller than `left`, it means this index is no longer inside the current window.

### 4. Record the maximum

```java
if (i >= k - 1) {
    ans[index++] = nums[deque.peekFirst()];
}
```

When `i >= k - 1`, the first complete window has formed.

The front of the deque is the index of the maximum value.

## Why Monotonic Queue Works

The queue is always decreasing by value.

Example:

```text
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
```

When we see `3`, the previous `1` is useless because:

- `3` is larger than `1`
- `3` appears later than `1`
- Any future window containing `1` and `3` will prefer `3`

So `1` can be removed.

This is the key idea of monotonic queue:

```text
Remove elements that can never become the answer.
```

## Mistakes and Notes

### Mistake 1: Storing values instead of indices

If we only store values, we cannot easily know whether the value is outside the window.

So we store indices:

```java
Deque<Integer> deque = new ArrayDeque<>();
```

Then use:

```java
nums[deque.peekFirst()]
```

to get the actual value.

### Mistake 2: Forgetting to remove expired indices

Current window left boundary:

```java
int left = i - k + 1;
```

Expired index:

```java
deque.peekFirst() < left
```

### Mistake 3: Updating answer too early

Only record answer after the first full window appears:

```java
if (i >= k - 1)
```

## Pattern

This problem is a classic monotonic queue problem.

Template:

```python
q = deque()

for i, num in enumerate(nums):
    while q and nums[q[-1]] <= num:
        q.pop()

    q.append(i)

    left = i - k + 1

    if q[0] < left:
        q.popleft()

    if i >= k - 1:
        ans.append(nums[q[0]])
```

## Review Notes

- Deque stores indices.
- Values in deque are decreasing.
- Front is always the maximum of the current window.
- Remove smaller values from the back.
- Remove expired indices from the front.
- Record answer only when `i >= k - 1`.