"""

See the file `01_is_2_colorable.md` in this repository for more information on this exercise.

"""


class Node:
    def __init__(self, name):
        self.name = name
        self.color = None
        self.neighbors = []

    def __str__(self):
        return f"Node(\"{self.name}\")"

    def __repr__(self):
        return f"Node(\"{self.name}\")"


def is_2_colorable(nodes):
    result = None
    """

    YOUR CODE GOES HERE

    """
    return result



#
# TESTS
#
print("K3")
A = Node("A")
B = Node("B")
C = Node("C")
A.neighbors = [B, C]
B.neighbors = [A, C]
C.neighbors = [A, B]
K3 = [A, B, C]
assert(is_2_colorable(K3) == False)

print("C4")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
A.neighbors = [B, D]
B.neighbors = [A, C]
C.neighbors = [B, D]
D.neighbors = [A, C]
C4 = [A, B, C, D]
assert(is_2_colorable(C4) == True)

print("K4")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
A.neighbors = [B, C, D]
B.neighbors = [A, C, C]
C.neighbors = [A, B, D]
D.neighbors = [A, C, D]
K4 = [A, B, C, D]
assert(is_2_colorable(K4) == False)

print("K33")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
A.neighbors = [D, E, F]
B.neighbors = [D, E, F]
C.neighbors = [D, E, F]
D.neighbors = [A, B, C]
E.neighbors = [A, B, C]
F.neighbors = [A, B, C]
K33 = [A, B, C, D, E, F]
assert(is_2_colorable(K33) == True)

print("B0B")
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")

A.neighbors = [B, C, D]
B.neighbors = [A, E]
C.neighbors = [A, E]
D.neighbors = [A, F]
E.neighbors = [B, C]
F.neighbors = [D, G, H]
G.neighbors = [F, H]
H.neighbors = [F, G]

B0B = [A, B, C, D, E, F, H]
assert(is_2_colorable(B0B) == False)
