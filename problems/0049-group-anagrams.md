# 49. Group Anagrams

## Link

https://leetcode.cn/problems/group-anagrams/

## Tags

`HashMap`, `String`, `Sorting`

## Problem Summary

Group words that are anagrams of each other.

## Core Idea

Two anagrams become the same string after sorting their characters.

Example:

```text
eat -> aet
tea -> aet
ate -> aet
```

So the sorted string can be used as the HashMap key.

## Java Solution

```java
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            List<String> list = map.get(key);
            if (list == null) {
                list = new ArrayList<>();
                map.put(key, list);
            }

            list.add(str);
        }

        return new ArrayList<>(map.values());
    }
}
```

## Python Solution

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)

        return list(groups.values())
```

## Complexity

Let `n` be the number of words and `m` be the max length of a word.

- Time: `O(n * m log m)`
- Space: `O(n * m)`

## Review Notes

- Python `sorted(word)` returns a list of characters.
- Use `''.join(...)` to turn the sorted characters back into a string key.
- `defaultdict(list)` avoids manually checking whether the key exists.
