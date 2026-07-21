# Prefix Sum

Prefix sum is used to quickly calculate the sum of a subarray.

## Basic Idea

For an array `nums`, define:

```text
preSum[i + 1] = preSum[i] + nums[i]
```

Then:

```text
sum(left, right) = preSum[right + 1] - preSum[left]
```

## Basic Template

```python
pre_sum = [0] * (len(nums) + 1)

for i in range(len(nums)):
    pre_sum[i + 1] = pre_sum[i] + nums[i]
```

Range query:

```python
range_sum = pre_sum[right + 1] - pre_sum[left]
```

## Prefix Sum + HashMap

For problems that ask for the number of subarrays with sum `k`, use a HashMap to count previous prefix sums.

Key formula:

```text
currentSum - previousSum = k
```

So:

```text
previousSum = currentSum - k
```

Template:

```python
prefix_count = {0: 1}
current_sum = 0
answer = 0

for num in nums:
    current_sum += num
    answer += prefix_count.get(current_sum - k, 0)
    prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1
```

## Representative Problems

| Problem | Collection | Key Idea |
|---|---|---|
| [303. Range Sum Query Immutable](../problems/0303-range-sum-query-immutable.md) | Prefix Sum Practice | Use `preSum[right + 1] - preSum[left]` |
| [560. Subarray Sum Equals K](../problems/0560-subarray-sum-equals-k.md) | Hot100 | Count previous prefix sums with HashMap |

## Common Mistakes

### Forgetting `preSum[0] = 0`

Using an extra leading zero makes the formula consistent.

```text
sum(left, right) = preSum[right + 1] - preSum[left]
```

### Forgetting `prefix_count = {0: 1}`

For subarray sum counting problems, this handles subarrays starting at index `0`.

### Using sliding window when negative numbers exist

If the array contains negative numbers, sliding window may not work.

Prefix sum is more reliable for subarray sum problems.