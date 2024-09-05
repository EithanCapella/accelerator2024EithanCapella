"""

In this exercise, you have a large bag of candy which you would like to divide
up into smaller bags and sell. Your function will take three items as input:

* the number n of pieces of candy
* an array of length k of bag sizes that you can sell
* another array of length k listing the price you can charge for each bag size

For example, this input:

n = 25
sizes =  [2, 3, 5, 10]
prices = [1, 2, 3, 5]

indicates that you have 25 pieces of candy, which can be divided up and sold in
2-piece bags for $1 each, 3-piece bags for $2 each, 5-piece bags for $3 each,
and 10-piece bags for $5 each.

Your function should determine the number of bags of each size to sell in order
to maximize revenue. There is no limit on the number of bags of each size that
you use, but the total number of pieces of candy cannot be greater than n.

The function should return an array of length k indicating how many bags of
each size to sell, and the total profit.

Examples:

With the input provided above, the correct output is:

([2, 7, 0, 0], 16)

which indicates that the maximum profit can be obtained by selling 2 2-piece
bags of candy and 7 3-piece bags for a total of 2 * $1 + 7 * $2 = $16

However, if the price of a 10-piece bag is increased from 5 to 8, so that
the input is:

n = 25
sizes =  [2, 3, 5, 10]
prices = [1, 2, 3, 8]

then the output will be:

([1, 1, 0, 2], 19)

indicating that the maximum profit can be obtained by selling 1 2-piece
bag of candy, 1 3-piece bag and 2 10-piece bags for a total of
1 * $1 + 1 * $2 + 2 * $8 = $19.

"""

def candy_max(n, sizes, prices):
    best_choice = None
    best_profit = None

    """

    YOUR CODE GOES HERE

    """
    return best_choice, best_profit


## Tests

n = 25
sizes = [2, 3, 5, 10]
prices = [1, 2, 3, 5]
assert candy_max(n, sizes, prices) == ([2, 7, 0, 0], 16)

n = 25
sizes = [2, 3, 5, 10]
prices = [1, 2, 3, 8]
assert candy_max(n, sizes, prices) == ([1, 1, 0, 2], 19)

n = 4
sizes = [1, 2, 3, 4, 5, 6, 7, 8]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
assert candy_max(n, sizes, prices) == ([0, 2, 0, 0, 0, 0, 0, 0], 10)

print("All tests passsed!")
