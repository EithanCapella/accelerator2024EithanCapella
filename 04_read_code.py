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
    ans = None
    #
    # YOUR CODE GOES HERE
    #
    return ans


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
