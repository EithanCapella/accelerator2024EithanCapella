# Print all "cousins" of a node in a binary tree

Two nodes are cousins if they are at the same level in the tree, but do not have
the same parent node. For example, in the following tree:

```
                                  1
                                /   \
                               /     \
                              /       \
                             /         \
                            /           \
                           2             3
                          / \           / \
                         /   \         /   \
                        /    |         |    \
                       4     5         6     7
                      / \    |\       /|    / \
                     /   |   | \     / |    |  \
                     8   9  10 11   12 13  14  15
```
the cousins of 4 are 6 and 7, and the cousins of 10 are 8, 9, 12, 13, 14 and 15.

The object class Node will be predefined, and each node will have a left child,
a right child and a number:

```python

class Node:
    def __init__(self, left, right, number):
        self.left = left
        self.right = right
        self.number = number
```

The function should accept the root node of a tree and a number as input, and return a list of the numbers of the nodes
that are cousins. For example, if the node `root` refers to the tree above, the function should return a list containing
these numbers (possibly in a different order) as the cousins for 10:

```python
>> ans = cousins(root, 10)
>> print(ans)
[8, 9, 12, 13, 14, 15]
```

The numbers of the cousins can be returned in any order.
