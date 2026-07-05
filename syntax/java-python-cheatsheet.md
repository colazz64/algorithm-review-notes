# Java to Python Syntax Cheatsheet

This note records common syntax differences I met while moving from Java to Python.

## 1. HashMap vs dict

| Operation | Java `HashMap` | Python `dict` |
|---|---|---|
| Declare | `Map<Character, Integer> map = new HashMap<>();` | `counter = {}` or `counter = dict()` |
| Insert / update | `map.put(key, value);` | `counter[key] = value` |
| Get with default | `map.getOrDefault(key, 0)` | `counter.get(key, 0)` |
| Check key exists | `map.containsKey(key)` | `key in counter` |
| Remove key | `map.remove(key)` | `counter.pop(key)` or `del counter[key]` |
| Values | `map.values()` | `counter.values()` |
| Empty check | `map.isEmpty()` | `len(counter) == 0` or `not counter` |

### Example: Valid Anagram

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

## 2. HashSet vs set

| Operation | Java `HashSet` | Python `set` |
|---|---|---|
| Declare | `Set<Character> set = new HashSet<>();` | `seen = set()` |
| Add | `set.add(x);` | `seen.add(x)` |
| Contains | `set.contains(x)` | `x in seen` |
| Remove | `set.remove(x)` | `seen.remove(x)` or `seen.discard(x)` |

### Example: Contains Duplicate

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

## 3. Basic Syntax

| Java | Python |
|---|---|
| `null` | `None` |
| `true` / `false` | `True` / `False` |
| `&&` | `and` |
| `||` | `or` |
| `else if` | `elif` |
| `{}` | indentation |
| `if (condition)` | `if condition:` |
| `i++` | `i += 1` |
| `arr.length` | `len(arr)` |
| `s.length()` | `len(s)` |
| `s.charAt(i)` | `s[i]` |

## 4. Class Method Calls

In Java, recursive calls inside a class can often be written directly:

```java
return isSameTree(p.left, q.left);
```

In Python, methods inside a class need `self.`:

```python
return self.isSameTree(p.left, q.left)
```

## 5. List Creation

```python
nums = [0] * n
matrix = [[0] * m for _ in range(n)]
```

The `_` means the loop variable is not used.

## 6. Integer Division

Python has two division operators:

```python
n / 10    # float division
n // 10   # integer division
```

When translating Java integer division like this:

```java
n = n / 10;
```

Python should usually use:

```python
n //= 10
```

## 7. Common Mistakes I Made

| Mistake | Correct Python |
|---|---|
| `map.put(key, value)` | `counter[key] = value` |
| `else if` | `elif` |
| `map.value` | `counter.values()` |
| missing `:` after `if` | `if condition:` |
| `TreeNode.val` when using an object | `root.val` |
| `isSameTree(...)` inside class | `self.isSameTree(...)` |
| `n /= 10` for integer digit extraction | `n //= 10` |

## 8. Pythonic Shortcut

For character counting, Python has `Counter`:

```python
from collections import Counter

Counter(s) == Counter(t)
```

But when learning HashMap logic, it is better to manually write the dict version first.
