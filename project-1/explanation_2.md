# Udacity - Data Structures and Algorithms - Project 1

## Problem 2 - Directory Traversal

A file system is modeled as a tree, which suggests a recursive solution. Each directory node is recursively traversed
to get its immediate children. Worst case is the recursive traversal visits all items in the tree:

Time Complexity:

1. Visiting all items: O(n)
1. When an item is found, each item is appended to a list in O(n) time

Space Complexity:

In the worst case, all files would be found which requires bulding a list that is the size
of the directory tree, thus making the worst case space complexity O(n) as well.
