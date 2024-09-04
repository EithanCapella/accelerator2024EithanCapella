"""

In this exercise you need to write a function that accepts as input a
2-dimensional (rectangular) array of integers and the number of rows and columns
in the array. The array represents a minefield. The array will have 1
representing each location with a mine and 0 representing each "safe" location.
You will then need to generate a list of all paths from position (0, 0) to
position (m - 1, n - 1), where m is the number of columns in the matrix and n is
the number of rows, that do not pass through any location with a mine. A path
may proceed from one cell to the cell on the right, that is from (i, j) to (i, j
+ 1), or from one position to the position below, that is from (i, j) to (i + 1,
j). Your function should return the paths as a list of lists of 2-tuples. For
example, the path indicated by "*" characters below:

    0 1 2 3 4
    =========
0 : * * * 0 0
1 : 0 1 * 0 0
2 : 0 0 * 1 0
3 : 0 0 * * *

would be represented as:

[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)]

"""

def minefield_paths(A, m, n):
    def dfs(x, y, path):
        
        if (x == m - 1) and (y == n - 1): #Position is Bottom-Right hence we reached the end
            result.append(path + [(x, y)])
            #print(str(result) + " Final Path")
            return
        
        #Check if we haven't reached a corner and the next position is a path
        if y + 1 < n and A[x][y + 1] == 0: #Move Right
            #print(str(path) + " Moved Right")
            dfs(x, y + 1, path + [(x, y)])
        
        
        if x + 1 < m and A[x + 1][y] == 0: #Move Down
            #print(str(path) + " Moved Down")
            dfs(x + 1, y, path + [(x, y)])

    
    result = []
    if A[0][0] == 0:  #Start from position 0,0 if this position is a path
        dfs(0, 0, [])
    
    print (str(result) + " Collection")
    print("---------------------")
    return result


# Examples

A = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
m = 4
n = 5
paths = minefield_paths(A, m, n)
assert(paths == [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4)],
 [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 4), (3, 4)],
 [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)],
 [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4)],
 [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4)],
 [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (3, 3), (3, 4)],
 [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]])


# In the following example there are no paths because position (0, 0) has a mine.
A = [
    [1, 0, 0],
    [0, 1, 0],
    [1, 1, 0]
]
m = 3
n = 3
paths = minefield_paths(A, m, n)
assert(paths == [])
