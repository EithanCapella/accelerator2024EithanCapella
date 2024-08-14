# Depth-first search in a binary tree

Your function's arguments will be a reference to the root node of a binary tree, and a key, which is a string value.
Each node in the tree has three properties: `left`, `right` and `label`, referring to the node's left child, right child
and name, respectively. Your function should implement a depth-first search strategy and return the first node it
encounters whose label matches the key. If no node in the tree has a matching label, the function should return `None`.
Your implementation should always check the left child of a node first.
