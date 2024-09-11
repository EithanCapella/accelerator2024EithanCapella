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
        return hash(self.index)
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.index == other.index and self.name == other.name


def dfs(root):
    """Perform a depth-first search (DFS) on the tree."""
    yield root
    for child in root.children:
        yield from dfs(child)

def dfsNonGenerator(root, array):
    array.append(root)
    
    for child in root.children:
        dfsNonGenerator(child, array)
    
    return array
    
    

# for node1 in dfs(root):
#     for node2 in dfs(root):
#         if node1 != node2:
#            YOUR CODE GOES HERE
#             if node1.name + node2.name in target:
                    #list.append(node1, node2)

def find_word_pairsGenerator(root, targets):
    
    result = []
    
    #print(list(dfs(root)))
    
    for node1 in dfs(root):
        for node2 in dfs(root):
            if node1 != node2:
                if node1.name + node2.name in targets:
                    result.append(str(node1) + "," + str(node2))
    
    print(result)
    return result
    
def find_word_pairs(root, targets):
    
    result = []
    
    #print(list(dfs(root)))
    array = dfsNonGenerator(root , [])
    
    #print(array)
    
    for node1 in array:
        for node2 in array:
            if node1 != node2:
                if node1.name + node2.name in targets:
                    result.append(str(node1) + "," + str(node2))
    
    print(result)
    return result


# Test the implementation
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

A.children = [B, H]
B.children = [C, G]
C.children = [D, E]
H.children = [I, J]
D.children = [F]
I.children = [K, L]
J.children = [M]

ans = find_word_pairs(A, targets)

# Expected output: a set of node pairs
expected_output = {
    (Node(11, "aff"), Node(12, "ect")), 
    (Node(11, "aff"), Node(3, "ord")), 
    (Node(11, "aff"), Node(13, "ord")), 
    (Node(10, "des"), Node(2, "ign")), 
    (Node(10, "des"), Node(7, "ign")), 
    (Node(4, "exp"), Node(12, "ect")), 
    (Node(9, "exp"), Node(12, "ect"))
}

assert set(ans) == expected_output, "Test failed"

print("Test passed")
