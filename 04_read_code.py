"""

Read code exercise

"""

class Node:
    """ Represents one node in the parse tree """
    def __init__(self, text):
        self.text = text
        self.children = []

    def __str__(self):
        if self.text is None:
            return "[root]"
        return f"'{self.text}'"

    def __repr__(self):
        if self.text is None:
            return "[root]"
        return f"'{self.text}'"

def _print_tree_level(node, level):
    if level == 0:
        print(str(node))
    else:
        print("  |" * (level - 1) + "  +- " + str(node))
    if len(node.children) > 0:
        for child in node.children:
            print("  |" * (level + 1))
            _print_tree_level(child, level + 1)

def print_tree(root_node):
    """ Prints a code tree """
    _print_tree_level(root_node, 0)

def split_lines(code):
    """ Splits multi-line string into a list of its non-empty lines """
    return [x for x in code.split("\n") if len(x.strip()) > 0]

def detect_indent(line):
    """ Identifies the indent level of a line of code """
    n = len(line)
    ns = 0
    for i in range(n):
        if line[i] != " ":
            break
        ns += 1
    if ns % 4 != 0:
        raise RuntimeError(f"Incorrect indent in line '{line}'")
    return 1 + int(ns / 4)

def parse_code(code):
    """ Parsing function """
    #ans = None
    #
    # Idea first split the text by the spaces with split_lines
    # Then create a new empty node as our root.
    #for each line in this list of splitLines we can detect the indent level and assign a new Node to that point 
    #
    linesList = split_lines(code) #Create a list of all words saving the indent
    rootNode = Node(None) #Create an empty initial Node
    stack = [(0,rootNode)] #We will use a tuple to store the indent level and its node.
    
    
    for line in linesList:
        newNode = Node(line.strip())
        indentLevel = detect_indent(line)
        
        #stack[-1] gives tge last item or most recently added node
        #Idea: currentLine is a child of the node of the stack, we exit when we found a parent node for the current line.
        while (stack and stack[-1][0] >= indentLevel): #Check that the current lines level is less or equal to the indent of the last Node in the stack.
            stack.pop() #Pop the nodes to find the correct parent node with a lower indent level
            
        stack[-1][1].children.append(newNode)
        
        stack.append((indentLevel, newNode)) #New node pushed unto the stack for the new position.
        
            
    return rootNode


CODE = '''
# this is a Python program
import itertools

def print_perms(items):
    for perm in itertools.permutations(items):
        print(perm)
            print("haha")
    print("done with permutations")

def print_combs(items, k):
    for comb in itertools.combinations(items, k):
        print(comb)
    print("done with combinations")


print_perms(["a", "b", "c"])
print_combs([1, 2, 3, 4, 5], 2)
'''

root = parse_code(CODE)
print_tree(root)

print('\n~~~~~~~~~~~2nd code~~~~~~~~~~~~\n')
CODE2 = """
# this is a Python program with more nested levels

for i in range(5):
    for j in range(5):
        for k in range(5):
            for n in range(5):
                print(i * j * k * n)
                    for n in range(5):
                        print(i * j * k * n)

"""
root2 = parse_code(CODE2)
print_tree(root2)
