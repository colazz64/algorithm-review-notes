# 438. Find All Anagrams in a String

## Metadata

| Field | Value |
|---|---|
| Source | LeetCode Hot 100 |
| Topics | Sliding Window, HashMap, String |
| Difficulty | Medium |
| Status | Done |
| Review Priority | High |

## Links

- LeetCode: https://leetcode.cn/problems/find-all-anagrams-in-a-string/
- Collection: [LeetCode Hot 100](../leetcode-hot100/README.md)
- Topic: [Sliding Window](../topics/sliding-window.md)

## Problem Summary

Given two strings `s` and `p`, return all start indices of `p`'s anagrams in `s`.

An anagram means the characters and their frequencies are the same, but the order can be different.

## Core Idea

Use a fixed-size sliding window.

The window size should always be `p.length()`.

Steps:

1. Count character frequency of `p`.
2. Slide a window over `s`.
3. Maintain the character frequency of the current window.
4. When the window size equals `p.length()`, compare the two frequency arrays.
5. If they are equal, add `left` to the result.

Since the strings contain lowercase English letters, we can use an array of size `26`.

## Java Solution

```java
class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] pCount = new int[26];

        for (char ch : p.toCharArray()) {
            pCount[ch - 'a']++;
        }

        int[] windowCount = new int[26];
        int left = 0;
        List<Integer> result = new ArrayList<>();

        for (int right = 0; right < s.length(); right++) {
            windowCount[s.charAt(right) - 'a']++;

            if (right - left + 1 > p.length()) {
                windowCount[s.charAt(left) - 'a']--;
                left++;
            }

            if (right - left + 1 == p.length()) {
                if (Arrays.equals(pCount, windowCount)) {
                    result.add(left);
                }
            }
        }

        return result;
    }
}
```

## Python Solution

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = [0] * 26
        window_count = [0] * 26
        result = []

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s)):
            window_count[ord(s[right]) - ord('a')] += 1

            if right - left + 1 > len(p):
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(p):
                if window_count == p_count:
                    result.append(left)

        return result
```

## Complexity

| Type | Complexity |
|---|---|
| Time | `O(n * 26)` |
| Space | `O(26)` |

Because comparing two arrays of size `26` is constant time, this can be treated as `O(n)`.

## Mistakes and Notes

### Character to index

Java:

```java
ch - 'a'
```

Python:

```python
ord(ch) - ord('a')
```

Both convert a lowercase character into an index from `0` to `25`.

Example:

```text
'a' -> 0
'b' -> 1
'c' -> 2
```

### Fixed-size window

The window must keep the same size as `p`.

When the window becomes too large:

```java
if (right - left + 1 > p.length()) {
    windowCount[s.charAt(left) - 'a']--;
    left++;
}
```

Python:

```python
if right - left + 1 > len(p):
    window_count[ord(s[left]) - ord('a')] -= 1
    left += 1
```

## Pattern

This is a fixed-size sliding window problem.

Template:

```python
left = 0

for right in range(len(s)):
    # add s[right]

    if window_size > k:
        # remove s[left]
        left += 1

    if window_size == k:
        # update answer
```

## Review Notes

- This problem is different from problem 3.
- Problem 3 uses a variable-size window.
- Problem 438 uses a fixed-size window.
- The window size is always `len(p)`.
- Frequency arrays are useful when the character set is fixed.