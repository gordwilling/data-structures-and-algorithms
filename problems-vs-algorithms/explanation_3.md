# Udacity - Data Structures and Algorithms - Project 2

## Problem 3 - Rearrange  Array Elements

Solving this problem involves two steps:

1. Sort the input list
1. Binary search the portion of the list where the value resides

Sorting uses a descending merge sort for worst case time complexity O(nlogn)

Arranging the digits involves traversing the input list once, for O(n) time complexity. The numbers are
arranged such that the highest numbers are placed in the most significant digit positions

In total, the time complexity is O(nlogn) + O(n), giving O(nlogn)

The space complexity is constant O(1) because the sort is done in place, and the numbers are always returned in a 
list of 2 elements


