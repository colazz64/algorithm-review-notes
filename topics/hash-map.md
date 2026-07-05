# HashMap and Set

## When to Use

Use HashMap or Set when the problem involves:

- checking whether something appeared before
- counting frequencies
- grouping items by a key
- finding complements, such as `target - nums[i]`

## Core Idea

Hash structures trade extra space for faster lookup.

Typical operations:

```python
seen = set()
counter = {}
counter[x] = counter.get(x, 0) + 1
```

## Pattern 1: Seen Set

Use a set when I only care whether a value appeared before.

Example: `217. Contains Duplicate`

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
```

## Pattern 2: Frequency Counter

Use a dict when I need to count how many times each value appears.

Example: `242. Valid Anagram`

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

## Pattern 3: Group by Key

Use a dict where the key represents the same group.

Example: `49. Group Anagrams`

Key idea:

```python
key = ''.join(sorted(word))
groups[key].append(word)
```

## Java to Python Mapping

| Java | Python |
|---|---|
| `HashSet` | `set` |
| `HashMap` | `dict` |
| `set.contains(x)` | `x in seen` |
| `map.getOrDefault(x, 0)` | `counter.get(x, 0)` |
| `map.put(k, v)` | `counter[k] = v` |

## Common Mistakes

- Do not write `map.put()` in Python.
- Do not write `else if`; Python uses `elif`.
- Do not write `map.value`; use `map.values()`.
- If using `pop()` when count becomes zero, the final check can be `len(counter) == 0`.
