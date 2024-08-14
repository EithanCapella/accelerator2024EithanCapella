"""

Binary search implementation

"""
from typing import List

def binary_search(items: List[int], key: int) -> int:
    """

    Binary search implementation.

    Parameters
    ----------

    items : List[int]

        List of numbers to search. This list will always be sorted in ascending order

    key : int

        Item to search for

    Returns
    -------

    int

        Index of key in list of items, or -1 if it is not present

    """
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
items = [0, 2, 3, 8, 9]
key = 8
result = binary_search(items, key)
expected = 3
assert result == expected, f"Wrong answer with items = {items}, key = {key}"

#
# Simple example - key is not present
#
items = [0, 2, 3, 8, 9]
key = 4
result = binary_search(items, key)
expected = -1
assert result == expected, f"Wrong answer with items = {items}, key = {key}"

#
# Item is present more than once
#
items = [0, 2, 2, 8, 8]
key = 8
result = binary_search(items, key)
expected = 3
assert result == expected, f"Wrong answer with items = {items}, key = {key}"

#
# List is empty
#
items = []
key = 2
result = binary_search(items, key)
expected = -1
assert result == expected, f"Wrong answer with items = {items}, key = {key}"

#
# Key is at the beginning of the list
#
items = [0, 2, 3, 8, 9]
key = 0
result = binary_search(items, key)
expected = 0
assert result == expected, f"Wrong answer with items = {items}, key = {key}"

#
# Key is at the end of the list
#
items = [0, 2, 3, 8, 9]
key = 9
result = binary_search(items, key)
expected = 4
assert result == expected, f"Wrong answer with items = {items}, key = {key}"

print("All tests passed!")
