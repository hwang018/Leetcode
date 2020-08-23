Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Idea:
1. Recursive solution:

if root is None: 
    return 0
else:
    return max(max_depth(root.left), max_depth(root.left)) +1
    
2. Tail recursion
(Python not supporting this)

3. Iterative solution
using stack to store current node and its depth
