# Binary search

Given a list of integers sorted in ascending order, and an individual integer key, return the index of the first index in the list
for which the associated list item is equal to the key. If no item in the list is equal to the key, return -1.

## Examples

### Simple example - key is present
```
>> items = [0, 2, 3, 8, 9]
>> key = 8
>> result = binary_search(items, key)
>> print(result)
3
```

### Simple example - key is not present
```
>> items = [0, 2, 3, 8, 9]
>> key = 4
>> result = binary_search(items, key)
>> print(result)
-1
```

### Item is present more than once
```
>> items = [0, 2, 2, 8, 8]
>> key = 8
>> result = binary_search(items, key)
>> print(result)
3
```

### List is empty
```
>> items = []
>> key = 2
>> result = binary_search(items, key)
>> print(result)
-1
```

### Key is at the beginning of the list
```
>> items = [0, 2, 3, 8, 9]
>> key = 0
>> result = binary_search(items, key)
>> print(result)
0
```

### Key is at the end of the list
```
>> items = [0, 2, 3, 8, 9]
>> key = 9
>> result = binary_search(items, key)
>> print(result)
4
```
