# Count seating arrangements

Due to an ongoing pandemic, a theater has been told that regulations will be put into place governing how close people in the same row of seats may be to each other. 
Being a very old and poorly maintained theater, they already have several missing seats! If there are `n` seats in a row, we have `n-1` distances between them. For this
task, you will need to implement a function called `seating_arrangements` that takes two arguments: a list `sd` of the `n-1` distances, and a value `md` which is the 
minimum distance allowed. The function should return the number of distinct seating arrangements for the row in which no two persons are less than `md` units apart.

For example, suppose a row contains four seats:

```
SEAT <- 2ft -> SEAT <- 3ft -> SEAT <- 1ft -> SEAT
```

and the minimum allowed distance is 5 feet. Then the following seating arrangements are allowed (where 1 represents a filled seat and 0 represents and empty seat):

```
0000
0001
0010
0100
1000
1001
1010
```

so `seating_arrangements([2, 3, 1], 5)` should return `7`.
