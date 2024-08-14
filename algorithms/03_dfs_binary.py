"""

Implementation of DFS for a binary tree

"""

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


def dfs_binary(root: Node, key: str) -> Node:
    """

    Conduct a depth-first search of the tree whose root node is provided and return the first node whose label matches
    the passed key, or None if no such node exists.

    Parameters
    ----------

    root : Node

        Root node of the tree

    key : str

        Value to search for among node labels

    Returns
    -------

    Node

        First node encountered with a matching label, or None if no such node exists

    """
    result = None
    #
    # YOUR CODE GOES HERE
    #
    return result

#
# TESTS
#

#
#    A
#   / \
#  /   \
#  B   C
# / \ / \
# D E F G
#
n0 = Node("A")
n00 = Node("B")
n01 = Node("C")
n000 = Node("D")
n001 = Node("E")
n010 = Node("F")
n011 = Node("G")

key = "E"
result = dfs_binary(n0, key)
expected = n001
assert result is expected

key = "Q"
result = dfs_binary(n0, key)
expected = None
assert result is expected

#
#
#    A
#   / \
#  /   \
#  B   C
# / \ / \
# C A D D
#
n0 = Node("A")
n00 = Node("B")
n01 = Node("C")
n000 = Node("C")
n001 = Node("A")
n010 = Node("D")
n011 = Node("D")

key = "C"
result = dfs_binary(n0, key)
expected = n00
assert result is expected

key = "D"
result = dfs_binary(n0, key)
expected = n010
assert result is expected

