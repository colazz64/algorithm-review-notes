# Sliding Window

## When to Use

Use sliding window when the problem asks about a continuous subarray or substring, especially:

- fixed length `k`
- maximum or minimum value inside a window
- number of valid windows
- replacing a brute force nested loop over subarrays

## Fixed-Size Window Idea

For a window of size `k`, each step does three things:

1. Add the new right-side element.
2. When the window size reaches `k`, update the answer.
3. Remove the left-side element before moving forward.

## Python Template

```python
window = 0
ans = 0

for i in range(n):
    window += value_of(nums[i])

    if i < k - 1:
        continue

    ans = update(ans, window)

    window -= value_of(nums[i - k + 1])
```

## Java Template

```java
int window = 0;
int ans = 0;

for (int i = 0; i < n; i++) {
    window += valueOf(nums[i]);

    if (i < k - 1) {
        continue;
    }

    ans = Math.max(ans, window);

    window -= valueOf(nums[i - k + 1]);
}
```

## Problem 1456: Maximum Number of Vowels in a Substring of Given Length

### Mistake

The brute force solution checks every substring of length `k`, so it repeats a lot of work and can time out.

### Core Idea

Maintain the number of vowels inside the current window.

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        ans = 0

        for i in range(len(s)):
            if s[i] in vowels:
                count += 1

            if i < k - 1:
                continue

            ans = max(ans, count)

            if s[i - k + 1] in vowels:
                count -= 1

        return ans
```

## Problem 643: Maximum Average Subarray I

### Core Idea

Maximum average of length `k` is the same as maximum sum of length `k`.

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0
        max_sum = float('-inf')

        for i in range(len(nums)):
            window_sum += nums[i]

            if i < k - 1:
                continue

            max_sum = max(max_sum, window_sum)
            window_sum -= nums[i - k + 1]

        return max_sum / k
```

## Problem 1343: Number of Sub-arrays of Size K and Average Greater Than or Equal to Threshold

### Better Check

Instead of computing average every time, compare sum directly:

```python
window_sum >= k * threshold
```

```python
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = 0
        ans = 0
        target = k * threshold

        for i in range(len(arr)):
            window_sum += arr[i]

            if i < k - 1:
                continue

            if window_sum >= target:
                ans += 1

            window_sum -= arr[i - k + 1]

        return ans
```

## Common Mistakes

- Updating the answer before the window reaches size `k`.
- Forgetting to remove the left-side element.
- Using `i - k` instead of `i - k + 1`.
- Recomputing the whole window sum every time.
## Representative Problems

| Problem | Collections | Window Type | Key Idea |
|---|---|---|---|
| [3. Longest Substring Without Repeating Characters](../problems/0003-longest-substring-without-repeating-characters.md) | Hot100, NeetCode150 | Variable-size | Move `left` when a duplicate character appears |
| [438. Find All Anagrams in a String](../problems/0438-find-all-anagrams-in-a-string.md) | Hot100 | Fixed-size | Keep window size equal to `len(p)` and compare frequency counts |

## Variable-size Sliding Window

Used when the window size is not fixed and depends on whether the current window is valid.

Example:

```python
left = 0

for right in range(len(s)):
    # add s[right]

    while window is invalid:
        # remove s[left]
        left += 1

    # update answer
```

Problem 3 can be optimized with a HashMap, so we can jump `left` directly instead of moving it one step at a time.

```python
left = max(left, last_seen[ch] + 1)
```

## Fixed-size Sliding Window

Used when the window size is fixed.

Example:

```python
left = 0

for right in range(len(s)):
    # add s[right]

    if right - left + 1 > k:
        # remove s[left]
        left += 1

    if right - left + 1 == k:
        # update answer
```

Problem 438 uses this pattern because every anagram of `p` must have length `len(p)`.