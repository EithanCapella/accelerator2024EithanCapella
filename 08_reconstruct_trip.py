"""

In this exercise you will need to write a function to reconstruct a travel
itinerary (a list of destinations) from a list of pairs of start- and
end-points. Each pair will consist of two airport codes. You know that the
traveler's trip begins and ends at San José, Costa Rica (airport code SJO).

You may assume that, other than San José, the traveler will not visit any city
more than once in a journey. If the pairs cannot be converted into a list of
stops, the function should raise a RuntimeError.

Examples:


sjo --> lax --> mx
   \            /
     \          /
        \    yyz
Input: [('LAX', 'MEX'), ('SJO', 'LAX'), ('MEX', 'YYZ'), ('YYZ', 'SJO')]
Output: ['SJO', 'LAX', 'MEX', 'YYZ', 'SJO']

Input: [('YYZ', 'ORD'), ('LAX', 'YVR'), ('YVR', 'YYZ'), ('SJO', 'JFK'), ('JFK', 'LAX'), ('ORD', 'SJO')]
Output: ['SJO', 'JFK', 'LAX', 'YVR', 'YYZ', 'ORD', 'SJO']

Input: [('YVR', 'JFK'), ('SJO', 'YVR'), ('MEX', 'SJO'), ('JFK', 'MEX')]
Output: ['SJO', 'YVR', 'JFK', 'MEX', 'SJO']

Input: [('LAX', 'MEX'), ('SJO', 'JFK'), ('MEX', 'SJO')]
Output: Error - there is no leg of the journey departing from JFK, and no
leg arriving at LAX.

Input: [('LAX', 'MEX'), ('SJO', 'LAX'), ('MEX', 'YYZ'), ('YYZ', 'SJO')]
Output: ['SJO', 'LAX', 'MEX', 'YYZ', 'SJO']
"""
def reconstruct(hops):
    result = None
    #
    # YOUR CODE GOES HERE
    #

    return result


# Tests
TEST_NO = 1
INPUT = [('LAX', 'MEX'), ('SJO', 'LAX'), ('MEX', 'YYZ'), ('YYZ', 'SJO')]
EXPECTED = ['SJO', 'LAX', 'MEX', 'YYZ', 'SJO']
RESULT = reconstruct(INPUT)
if RESULT != EXPECTED:
    raise RuntimeError(f"Error in test {TEST_NO} with input {repr(INPUT)}, expected {repr(EXPECTED)} but result was {repr(RESULT)}")

TEST_NO = 2
INPUT = [('YYZ', 'ORD'), ('LAX', 'YVR'), ('YVR', 'YYZ'), ('SJO', 'JFK'), ('JFK', 'LAX'), ('ORD', 'SJO')]
EXPECTED = ['SJO', 'JFK', 'LAX', 'YVR', 'YYZ', 'ORD', 'SJO']
RESULT = reconstruct(INPUT)
if RESULT != EXPECTED:
    raise RuntimeError(f"Error in test {TEST_NO} with input {repr(INPUT)}, expected {repr(EXPECTED)} but result was {repr(RESULT)}")

TEST_NO = 3
INPUT = [('YVR', 'JFK'), ('SJO', 'YVR'), ('MEX', 'SJO'), ('JFK', 'MEX')]
EXPECTED = ['SJO', 'YVR', 'JFK', 'MEX', 'SJO']
RESULT = reconstruct(INPUT)
if RESULT != EXPECTED:
    raise RuntimeError(f"Error in test {TEST_NO} with input {repr(INPUT)}, expected {repr(EXPECTED)} but result was {repr(RESULT)}")

TEST_NO = 4
INPUT = [('LAX', 'MEX'), ('SJO', 'JFK'), ('MEX', 'SJO')]
thrown = False
try:
    reconstruct(INPUT)
except RuntimeError as _:
    thrown = True
if not(thrown):
    raise RuntimeError(f"Expected error to be thrown with input {repr(INPUT)} but that did not happen")
