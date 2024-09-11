"""

In this exercise you will need to write a function that accepts the root node of
a tree and a list of strings as input. Each node of the tree will have a numeric
index and a name. The strings will be words of the same length, and each node
name will be half the length of the words. The function should return a list of
all pairs of nodes in the tree whose names can be concatenated to form one of
the words in the list.

Example:

Tree:

1, twe
 |
 + 2, ign
 |  |
 |  + 3, ord
 |  |  |
 |  |  + 4, exp
 |  |  |
 |  |  + 5, sim
 |  |
 |  + 6, let
 |     |
 |     + 7, ign
 |
 + 8, ort
    |
    + 9, exp
    |  |
    |  + 10, des
    |  |
    |  + 11, aff
    |
    + 12, ect
    |
    + 13, ord

List of words: ["affect", "afford", "desert", "design", "expect", "expert"]

Output:
[
    (Node(11, "aff"), Node(12, "ect")), 
    (Node(11, "aff"), Node(3, "ord")), 
    (Node(11, "aff"), Node(13, "ord")), 
    (Node(10, "des"), Node(2, "ign")), 
    (Node(10, "des"), Node(7, "ign")), 
    (Node(4, "exp"), Node(12, "ect")), 
    (Node(9, "exp"), Node(12, "ect"))
]

"""

class Node:
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.children = []
        
    def __str__(self):
        return f'Node({self.index}, "{self.name}")'
    
    def __repr__(self):
        return f'Node({self.index}, "{self.name}")'
        
    def __hash__(self):
        return hash(self.index, self.__delattr__
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.index == other.index and self.name == other.name


#
# for node1 in dfs(root):
#     for node2 in dfs(root):
#         if node1 != node2:
#            YOUR CODE GOES HERE
#             if node1.name + node2.name in target:
                    #list.append(node1, node2)
#
        
#
#   NodeHash ex. ord: [Node(3, "ord"), Node(13, "ord")]
#       for val in targets:
#       h1 = val[:len(val)/2]
#       h2 = val[len(val)/2:len(val)]
#       if h1 in NodeHash and h2 in NodeHash:
#           for side1 in NodeHash[h1]:
#               for side2 in NodeHash[h2]:
                    #result.append(side1,side2)
            


def find_word_pairs(root, targets):
    #
    # YOUR CODE GOES HERE
    #
    for word in targets:
        leftHalf = word[:len(word)/2]
    
    nodeA = root
    nodeB = None
    
    # ord: [Node(3, "ord"), Node(13, "ord")]
    
    #Find the
    
    #
    
    #aff : ect
    #aff : ord
    

    #aff, des, exp
    #ect, ord, ert, ign
    
    #aff
    
    #affert not in target
    
## Examples
targets = ['affect', 'afford', 'desert', 'design', 'expect', 'expert']

A = Node(1, "twe")
B = Node(2, "ign")
C = Node(3, "ord")
D = Node(4, "exp")
E = Node(5, "sim")
F = Node(6, "let")
G = Node(7, "ign")
H = Node(8, "ort")
I = Node(9, "exp")
J = Node(10, "des")
K = Node(11, "aff")
L = Node(12, "ect")
M = Node(13, "ord")

A.children = [B, C]
B.children = [D, E]
C.children = [F, G, H]
D.children = [I, J]
E.children = [K]
F.children = [L, M]

ans = find_word_pairs(A, targets)

assert(set(ans) == {(Node(11, "aff"), Node(12, "ect")), (Node(11, "aff"), Node(3, "ord")), (Node(11, "aff"), Node(13, "ord")), (Node(10, "des"), Node(2, "ign")), (Node(10, "des"), Node(7, "ign")), (Node(4, "exp"), Node(12, "ect")), (Node(9, "exp"), Node(12, "ect"))}


        
