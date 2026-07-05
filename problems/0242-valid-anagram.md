# 242. Valid Anagram

## Link

https://leetcode.cn/problems/valid-anagram/

## Tags

`String`, `HashMap`, `dict`, `Counting`

## Problem Summary

Return `true` if two strings contain the same characters with the same frequencies.

## My Mistake

I mixed Java HashMap syntax into Python:

```python
map.put(ch, map[ch])
else if
map.value
```

Correct Python syntax:

```python
counter[ch] = value
elif
counter.values()
```

## Core Idea

Count characters in `s`, then use characters in `t` to cancel the counts.  
If every character is canceled, the dictionary should be empty.

## Java Solution

```java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> map = new HashMap<>();

        for (char ch : s.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for (char ch : t.toCharArray()) {
            if (!map.containsKey(ch)) {
                return false;
            }

            int count = map.get(ch);
            if (count == 1) {
                map.remove(ch);
            } else {
                map.put(ch, count - 1);
            }
        }

        return map.isEmpty();
    }
}
```

## Python Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1

        for ch in t:
            if ch not in counter:
                return False

            if counter[ch] == 1:
                counter.pop(ch)
            else:
                counter[ch] -= 1

        return len(counter) == 0
```

## Complexity

- Time: `O(n)`
- Space: `O(k)`, where `k` is the number of unique characters

## Review Notes

- Python string can be directly looped with `for ch in s`.
- `dict.get(key, 0)` is Python's version of Java `getOrDefault`.
- If count becomes zero and I remove the key, final check is `len(counter) == 0`.
