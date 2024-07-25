# Pivot point

Write a function called `pivot_point` that accepts as input an array `x` of integers. The method should find and return the index `i` of the first element of the array such that the sum of all elements in the array from position `0` through `i - 1` is the same as the sum of all elements from position `i + 1` through `len(x) - 1`. If no such element exists, the method should return `-1`.

## Examples

```python
>> x = [9, -2, 4, 8, 6, 4, 1]
>> y = pivot_point(x)
>> print(y)

3
```

```python
>> x = [-1, 1, 0]
>> y = pivot_point(x)
>> print(y)

2
```

```python
>> x = [0, -2, 1, 1]
>> y = pivot_point(x)
>> print(y)

0
```

```python
>> x = []
>> y = pivot_point(x)
>> print(y)

-1
```

## Bonus question (more math than coding)

Write another function called `all_pivots` that does not stop when it finds one pivot point, but prints all of the pivot points it finds. Can you find a 5-element array that has more than one pivot point?
