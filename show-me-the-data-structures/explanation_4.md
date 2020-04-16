# Udacity - Data Structures and Algorithms - Project 1

## Problem 4 - Active Directory

In Active Directory, groups can contain users and sub groups. As such, groups can be represented hierarchically in a 
tree structure where each group is a node. Determining if a user is in a group involves traversing the tree to find
the group or subgroup containing the user. 

1. Traversing the tree can be done recursively. Finding a particular user requires - at worst - visiting each node in the tree, thus the worst case time complexity for traversal is O(n).
1. At each step in the traversal we search for a specific user in a set, which is an O(1) operation. 

Space complexity is constant O(1) because the operation only requires tracking a few pointers as the tree is traversed.
