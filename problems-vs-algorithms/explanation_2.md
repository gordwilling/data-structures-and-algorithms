# Udacity - Data Structures and Algorithms - Project 2

## Problem 2 - Search in a Rotated Sorted Array

Solving this problem involves two steps:

1. Find the index of the start of the sorted list (the lowest value in the list)
1. Binary search the portion of the list where the value resides

Both steps can be done using binary search O(logn). In the first step, the binary search is for two adjacent values in 
the list where the left value is larger than the right value. This is the boundary

Because the sublists on either side of the boundary are sorted, we know which section of the list to feed to the next 
binary search for the target value, another O(logn)

Time Complexity is 2 * logn, or just O(logn) 

Space complexity is constant; no data structures are used - only index tracking