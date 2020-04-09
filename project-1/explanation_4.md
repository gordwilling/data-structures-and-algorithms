# Udacity - Data Structures and Algorithms - Project 1

## Problem 4 - Active Directory

In Active Directory, groups can contain users and sub groups. As such, groups can be represented hierarchically in a 
tree structure where each group is a node. Determining if a user is in a group involves traversing the tree to find
the the group or subgroup containing the user. Traversing the tree can be done recursively and finding a particular 
user requires - at worst - visiting each node in the tree, thus the worst case time complexity is O(n).
