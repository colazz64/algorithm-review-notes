# Two Pointers

Two pointers are useful when the problem involves scanning an array/string from both sides or maintaining a write position during in-place modification.

## Patterns

### 1. Opposite Direction Pointers

Use `left` and `right` from both ends.

Representative problems:

| Problem | Collections | Key Idea |
|---|---|---|
| [11. Container With Most Water](../problems/0011-container-with-most-water.md) | Hot100, NeetCode150 | Move the shorter wall |

### 2. Fast/Slow or Read/Write Pointers

Use one pointer to scan and another pointer to write or maintain a boundary.

Representative problems:

| Problem | Collections | Key Idea |
|---|---|---|
| [283. Move Zeroes](../problems/0283-move-zeroes.md) | Hot100 | `i` scans, `j` points to next non-zero position |

## Template

```
```python
j = 0

for i in range(len(nums)):
    if condition(nums[i]):
        nums[i], nums[j] = nums[j], nums[i]
        j += 1

```


