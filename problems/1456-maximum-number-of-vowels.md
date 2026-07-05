# 1456. Maximum Number of Vowels in a Substring of Given Length

## Link

https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

## Tags

`String`, `Sliding Window`, `Set`

## Problem Summary

Given a string `s` and an integer `k`, find the maximum number of vowels in any substring of length `k`.

## My Mistake

The first idea was brute force:

- enumerate every substring of length `k`
- count vowels inside each substring

This repeats too much work and can time out.

## Core Idea

Use a fixed-size sliding window.

For each index:

1. Add the new character on the right.
2. If the window reaches size `k`, update the answer.
3. Remove the old character on the left.

## Java Solution

```java
class Solution {
    public int maxVowels(String s, int k) {
        HashSet<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int ans = 0;
        int count = 0;
        char[] chars = s.toCharArray();

        for (int i = 0; i < chars.length; i++) {
            if (vowels.contains(chars[i])) {
                count++;
            }

            if (i < k - 1) {
                continue;
            }

            ans = Math.max(ans, count);

            if (vowels.contains(chars[i - k + 1])) {
                count--;
            }
        }

        return ans;
    }
}
```

## Python Solution

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

## Complexity

- Time: `O(n)`
- Space: `O(1)`

## Review Notes

- `i - k + 1` is the left boundary of the current window.
- Update answer before removing the left element.
- Python set literal can be written as `{'a', 'e', 'i', 'o', 'u'}`.
