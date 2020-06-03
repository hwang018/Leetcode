Invert a binary tree.

Idea:
if a tree is empty, its inverse also empty (corner case)
else
the inversed tree's left is the inverse of the original tree's right (due to another inverse at root level)
the inversed tree's right is the inverse of the original tree's left (due to another inverse at root level)

therefore we do it recursively.

