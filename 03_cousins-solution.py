"""

Cousins exercise

"""
class Node:
    """ Represents a binary tree node """
    def __init__(self, left, right, number):
        self.left = left
        self.right = right
        self.number = number

def cousins(root, number):
    """ Cousins implementation """
    ans = []
    #
    # YOUR CODE GOES HERE
    #
    
    #We want to find the siblings or given Node first
    
    target_node_parent = None
    target_node_level = None
    
    queue = []
    queue.append((root, 1))
    
    while (len(queue) != 0):
        current, current_level = queue.pop(0)
        print("current: " + str(current.number) + " level: " + str(current_level))
        
        if(current.left.number == number or current.right.number == number): 
            found = True
            target_node_parent = current
            target_node_level = current_level + 1
            
            break
        
        queue.append((current.left, current_level + 1))
        queue.append((current.right, current_level + 1))
    
    print(str(target_node_parent.number) + " " + str(target_node_level))
      
    queue = [] 
    queue.append((root, 1))
    
    while (len(queue) != 0):
        current, current_level = queue.pop(0)
        
        if (current_level == target_node_level - 1 and current.number != target_node_parent.number):
            if (current.left is not None and current.right is not None):
                ans.append(current.left.number)
                ans.append(current.right.number)
        
        if (current.left is not None and current.right is not None):
            queue.append((current.left, current_level + 1))
            queue.append((current.right, current_level + 1))
        
        
        
        
        
    
    #if parent.left.number == number or parent.right.number == number:
    
    #else:
        #if (p.left)
        #append to array
        
    return ans


#
# TESTS
#
n08 = Node(None, None, 8)
n09 = Node(None, None, 9)
n10 = Node(None, None, 10)
n11 = Node(None, None, 11)
n12 = Node(None, None, 12)
n13 = Node(None, None, 13)
n14 = Node(None, None, 14)
n15 = Node(None, None, 15)
n04 = Node(n08, n09, 4)
n05 = Node(n10, n11, 5)
n06 = Node(n12, n13, 6)
n07 = Node(n14, n15, 7)
n02 = Node(n04, n05, 2)
n03 = Node(n06, n07, 3)
n01 = Node(n02, n03, 1)

nn = 10
result = cousins(n01, nn)
expected = [8, 9, 12, 13, 14, 15]
assert set(result) == set(expected), f"Wrong answer for node {nn}"

nn = 2
result = cousins(n01, nn)
expected = []
assert set(result) == set(expected), f"Wrong answer for node {nn}"

nn = 6
result = cousins(n01, nn)
expected = [4, 5]
assert set(result) == set(expected), f"Wrong answer for node {nn}"

nn = 11
result = cousins(n01, nn)
expected = [8, 9, 12, 13, 14, 15]
assert set(result) == set(expected), f"Wrong answer for node {nn}"

print("Tests passed!")
