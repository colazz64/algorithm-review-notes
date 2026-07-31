
## Maximum Subarray / Kadane Algorithm

Representative problem:

- [53. Maximum Subarray](../problems/0053-maximum-subarray.md)

This is a one-dimensional DP problem.

Define:

```text
currentSum = maximum subarray sum ending at current index
```

Transition:

```text
currentSum = max(currentSum + nums[i], nums[i])
maxSum = max(maxSum, currentSum)
```

The key decision is:

```text
continue previous subarray or start a new subarray
```

Java:

```java
currentSum = Math.max(currentSum + nums[i], nums[i]);
maxSum = Math.max(maxSum, currentSum);
```

Python:

```python
current_sum = max(current_sum + nums[i], nums[i])
max_sum = max(max_sum, current_sum)
```

Common mistake:

Do not initialize `maxSum` as `0`, because the array may contain only negative numbers.