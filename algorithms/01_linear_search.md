# Linear search

Given a list of items which may be in any order, and an individual key, return the index of the first index in the list
for which the associated list item is equal to the key. If no item in the list is equal to the key, return -1.

## Examples

### Simple example - key is present
```
>> items = [8, 2, 0, 3, 9]
>> key = 2
>> result = linear_search(items, key)
>> print(result)
1
```

### Simple example - key is not present
```
>> items = [8, 2, 0, 3, 9]
>> key = 4
>> result = linear_search(items, key)
>> print(result)
-1
```

### Item is present more than once
```
>> items = [8, 2, 0, 2, 8]
>> key = 2
>> result = linear_search(items, key)
>> print(result)
1
```

### List is empty
```
>> items = []
>> key = 2
>> result = linear_search(items, key)
>> print(result)
-1
```


