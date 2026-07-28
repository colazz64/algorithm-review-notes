# Monotonic Queue

A monotonic queue is a deque that keeps elements in increasing or decreasing order.

It is useful for sliding window maximum or minimum problems.

## When to Use

Use monotonic queue when the problem asks for:

```text
maximum / minimum value in every window
```

Typical keywords:

- sliding window maximum
- sliding window minimum
- fixed-size window
- need max/min repeatedly

## Core Idea

For sliding window maximum, maintain a decreasing deque.

The front of the deque is always the maximum value of the current window.

Usually, we store indices instead of values.

Why?

Because indices allow us to check whether an element is outside the current window.

## Java Template

```java
Deque<Integer> deque = new ArrayDeque<>();

for (int i = 0; i < nums.length; i++) {
    while (!deque.isEmpty() && nums[deque.peekLast()] <= nums[i]) {
        deque.pollLast();
    }

    deque.offerLast(i);

    int left = i - k + 1;

    while (!deque.isEmpty() && deque.peekFirst() < left) {
        deque.pollFirst();
    }

    if (i >= k - 1) {
        ans[index++] = nums[deque.peekFirst()];
    }
}
```

## Python Template

```python
from collections import deque

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

## Representative Problems

| Problem | Collection | Key Idea |
|---|---|---|
| [239. Sliding Window Maximum](../problems/0239-sliding-window-maximum.md) | Hot100 | Decreasing deque stores indices |

## Common Mistakes

### Store values instead of indices

Wrong idea:

```text
deque stores nums[i]
```

Better idea:

```text
deque stores i
```

Because we need to remove expired indices.

### Forget expired elements

Current window left boundary:

```text
left = i - k + 1
```

If:

```text
deque.peekFirst() < left
```

then the front index is outside the window.

### Confuse queue order and value order

The deque order is by index from old to new.

But the values are monotonic:

```text
nums[deque[0]] >= nums[deque[1]] >= nums[deque[2]]
```