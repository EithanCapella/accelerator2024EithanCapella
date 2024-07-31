Convert source code to tree
---------------------------

Write a function that reads a string containing lines of Python code and
produces a tree. The tree will have a root node with no text that represents the
program as a whole. Lines of code that have no spaces at the beginning (that is,
lines that are not indented) will be child nodes of the root node. Other lines
will be children of other nodes according to their indentation. Blank lines
should be ignored. For example, if the input looks like this:

```python
# this is a Python program
import itertools

def print_perms(items):
    for perm in itertools.permutations(items):
        print(perm)
    print("done with permutations")

def print_combs(items, k):
    for comb in itertools.combinations(items, k):
        print(comb)
    print("done with combinations")

print_perms(["a", "b", "c"])
print_combs([1, 2, 3, 4, 5], 2)
```

then the output should be a tree like this:

```txt
[root]
  |
  +- '# this is a Python program'
  |
  +- 'import itertools'
  |
  +- 'def print_perms(items):'
  |  |
  |  +- 'for perm in itertools.permutations(items)'
  |  |  |
  |  |  +- 'print(perm)'
  |  |
  |  +- 'print("done with permutations")'
  |
  +- 'def print_combs(items, k):'
  |  |
  |  +- 'for comb in itertools.combinations(items, k):'
  |  |  |
  |  |  +- 'print(comb)'
  |  |
  |  +- 'print("done with combinations")'
  |
  +- 'print_perms(["a", "b", "c"])'
  |
  +- 'print_combs([1, 2, 3, 4, 5], 2)'
```

The following functions have already been written:

* `print_tree` - outputs a tree in the format above
* `split_lines` - splits the lines of code into a list of strings, ignoring empty lines but preserving leading spaces
* `detect_indent` - given a line of code with leading spaces, computes and returns the level of indentation (1 if no indentation, 2 if there are 4 spaces, etc.)

HINT: Since it is possible with every new line to either indent or "outdent",
you will need to be able to add the current line to the list of children to one
of several different nodes, depending on the indentation. For example, consider
the line with code:

```python
    print("done with permutations")
```

Which node will this line be a child of?


