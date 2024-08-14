"""

Linear search implementation

"""
from typing import List, Any

def linear_search(items: List[Any], key: Any) -> int:
    result = -1
    #
    # YOUR CODE GOES HERE
    #
    return result

#
# TESTS
#

#
# Simple example - key is present
#
items = [8, 2, 0, 3, 9]
key = 2
expected = 1
result = linear_search(items, key)
assert result == expected, f"Wrong answer for items={items}, key={key}"

#
# Simple example - key is not present
#
items = [8, 2, 0, 3, 9]
key = 4
expected = -1
result = linear_search(items, key)
assert result == expected, f"Wrong answer for items={items}, key={key}"

#
# Item is present more than once
#
items = [8, 2, 0, 2, 8]
key = 2
expected = 1
result = linear_search(items, key)
assert result == expected, f"Wrong answer for items={items}, key={key}"

#
# List is empty
#
items = []
key = 2
expected = -1
result = linear_search(items, key)
assert result == expected, f"Wrong answer for items={items}, key={key}"
