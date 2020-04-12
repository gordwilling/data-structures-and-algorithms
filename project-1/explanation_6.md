# Udacity - Data Structures and Algorithms - Project 1

## Problem 6 - Union and Intersection

Producing the union and intersection of two linked lists (of length n and m, respectively) requires *at least* visiting 
each element in each list. This translates to a time complexity of O(n + m), or just O(n) asymptotically.

### Union

In creation of the union, duplicate elements should not appear in the output set. If the elements of the input lists 
are added to a Set data structure, checking for existence only requires O(1) for each element, thus the 
union operation can be kept at O(n + M) time and space complexity if:

1. The elements of each list are added to the same Set
1. A new list representing the union is created from the Set
1. Create a new list from the union set.

### Intersection

Sets can also be used to optimize performance of the Intersection operation. By loading all elements from one of the
lists into a set, lookup can be done with O(1) time complexity.

1. Add elements of list 1 to a Set (set 1)
1. Create an empty Set representing the intersection
1. Iterate over the elements in list 2 
    1. for each element, check for its existence in set 1
        1. if it exists, it is part of the intersection; add it to the intersection set
1. Add the elements from the intersection set to a new list

This is also O(n + m) time and space complexity






