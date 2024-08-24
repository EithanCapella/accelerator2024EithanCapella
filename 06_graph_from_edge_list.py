"""

In this exercise you will need to create an object class (that is, a new type)
to represent a graph node, and then write a function that takes an "edge list"
as input and returns a graph defined using instances of the new class.

A graph is made up of nodes and edges. Each edge occurs between a pair of nodes.
An edge list is a way of defining a graph by listing its edges in the form of
pairs of names of nodes. The set of distinct names appearing in the edge list
describes the set of nodes of the graph, and the pairs in the edge list describe
the edges. For example, this edge list:

[
    ("A", "B"), ("B", "C"), ("A", "C")
]

describes a graph with three nodes, A, B, and C, with edges connecting each pair
of distinct nodes:

A --- B
 \   /
  \ /
   C

1. Create an object class called Node with properties "name" and "neighbors".
   "name" is for the name of the node and "neighbors" is for a list of the other
   nodes to which the node is connected. Note that the items in the "neighbors"
   list should be other Node instances, not strings or numbers.

2. Write a function called graph_from_edge_list which accepts as input a list of
   tuples of length 2, and returns a list of Node objects. The Node objects
   should be initialized with the names of the graph nodes and lists of their
   neighbors. Note that if nodes x and y are neighbors, then x should be
   included in y's list of neighbors, *and* y should be included in x's list of
   neighbors. Also note that you should not create more Node object instances
   than there are nodes in the graph; that is, if z is a neighbor of both x and
   y, then the Node instance for z in the returned list, the instance in x's
   list of neighbors and the instance in y's list of neighbors should all be the
   same instance.

"""

class Node:
    """

    YOUR CODE GOES HERE

    """

def graph_from_node_list(nodes):
    """ Create a graph from a node list """
    result = None
    #
    # YOUR CODE GOES HERE
    #
    return result


def check_node_names(expected_names, nodes):
    """

    This function is included in order to check output from test inputs.

    """
    node_names = [node.name for node in nodes]
    if sorted(expected_names) != sorted(node_names):
        raise RuntimeError("ERROR: Expected node names not found in list of nodes")


#
# Examples
#
INPUT_1 = [("A", "B"), ("A", "C"), ("C", "B")]
OUTPUT_1 = graph_from_node_list(INPUT_1)
if OUTPUT_1 is None:
    raise RuntimeError("ERROR: None returned for INPUT_1")

check_node_names(["A", "B", "C"], OUTPUT_1)
for node in OUTPUT_1:
    expected_neighbors = [name for name in ["A", "B", "C"] if name != node.name]
    check_node_names(expected_neighbors, node.neighbors)

INPUT_2 = [("0", "1"), ("1", "2"), ("2", "3"), ("3", "4"), ("4", "5"), ("5", "0"), ("3", "0")]
OUTPUT_2 = graph_from_node_list(INPUT_2)
if OUTPUT_2 is None:
    raise RuntimeError("ERROR: None returned for INPUT_2")

check_node_names(["0", "1", "2", "3", "4", "5"], OUTPUT_2)
for i in range(5):
    n1 = (i - 1) % 6
    n2 = (i + 1) % 6
    expected_neighbors = [str(n1), str(n2)]
    if i == 0 or i == 3:
        expected_neighbors.append(str(3 - i))
    node = next(n for n in OUTPUT_2 if n.name == str(i))
    check_node_names(expected_neighbors, node.neighbors)
