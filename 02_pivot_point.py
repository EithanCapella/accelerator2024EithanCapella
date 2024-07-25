from typing import List

def pivot_point(x: List[int]) -> int:
  """

  YOUR CODE GOES HERE

  """
  return -1


#
# TESTS
#
x = [9, -2, 4, 8, 6, 4, 1]
result = pivot_point(x)
assert result == 3

x = [4, -1, 1]
result = pivot_point(x)
assert result == 0

x = [-1, 1, 3]
result = pivot_point(x)
assert result == 2

x = [4, 3, 2]
result = pivot_point(x)
assert result == -1
