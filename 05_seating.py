def seating_arrangements(sd: List[int], md: int) -> int:
  result = 0
  """

  YOUR CODE GOES HERE

  """
  return result


#
# TESTS
#

sd = [2, 3, 1]
td = 5
ans = seating_arrangements(sd, td)
exp = 7
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [5, 2, 4, 1, 2]
td = 6
ans = seating_arrangements(sd, td)
exp = 16
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [2, 3, 2]
td = 6
ans = seating_arrangements(sd, td)
exp = 0
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"

sd = [9, 9, 9, 9]
td = 2
ans = seating_arrangements(sd, td)
exp = 16
assert exp == ans, f"Incorrect answer for sd = {sd}, td = {td}"
