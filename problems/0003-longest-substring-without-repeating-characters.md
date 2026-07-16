# 3. Longest Substring Without Repeating Characters

## Metadata

| Field | Value |
|---|---|
| Source | LeetCode Hot 100, NeetCode 150 |
| Topics | Sliding Window, HashMap, String |
| Difficulty | Medium |
| Status | Done |
| Review Priority | High |

## Links

- LeetCode: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
- Collection: [LeetCode Hot 100](../leetcode-hot100/README.md)
- Collection: [NeetCode 150](../neetcode150/README.md)
- Topic: [Sliding Window](../topics/sliding-window.md)

## Problem Summary

Given a string `s`, find the length of the longest substring without repeating characters.

A substring must be continuous.

## Core Idea

Use a sliding window.

- `right` scans the string.
- `left` marks the start of the current valid window.
- A HashMap records the latest index of each character.
- When a repeated character appears, move `left` to the right of its previous position.

The key is:

```text
left = max(left, last_seen[ch] + 1)
```

We use `max` because `left` should never move backward.

## Java Solution

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        char[] chars = s.toCharArray();
        int left = 0;
        int result = 0;

        Map<Character, Integer> map = new HashMap<>();

        for (int right = 0; right < chars.length; right++) {
            char ch = chars[right];

            if (map.containsKey(ch)) {
                left = Math.max(left, map.get(ch) + 1);
            }

            int currentLength = right - left + 1;
            result = Math.max(result, currentLength);

            map.put(ch, right);
        }

        return result;
    }
}
```

## Python Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        last_seen = {}

        for right, ch in enumerate(s):
            if ch in last_seen:
                left = max(left, last_seen[ch] + 1)

            current_length = right - left + 1
            result = max(result, current_length)

            last_seen[ch] = right

        return result
```

## Complexity

| Type | Complexity |
|---|---|
| Time | `O(n)` |
| Space | `O(k)` |

`k` is the number of unique characters in the string.

## Mistakes and Notes

### Why use `max`?

Suppose the string is:

```text
abba
```

When we reach the second `a`, the previous `a` is outside the current valid window.

If we directly write:

```java
left = map.get(ch) + 1;
```

`left` may move backward.

So we must write:

```java
left = Math.max(left, map.get(ch) + 1);
```

Python version:

```python
left = max(left, last_seen[ch] + 1)
```

## Pattern

This is a classic variable-size sliding window problem.

Template:

```python
left = 0
window = {}

for right in range(len(s)):
    # add s[right]

    while window is invalid:
        # remove s[left]
        left += 1

    # update answer
```

For this problem, we do not need a `while` loop because the HashMap tells us exactly where to move `left`.