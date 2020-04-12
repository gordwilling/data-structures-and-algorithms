# Udacity - Data Structures and Algorithms - Project 1

## Problem 1 - LRU Cache

The LRU cache provides get and set operations with O(1) time complexity and O(n) space complexity.

A doubly-linked-list is used as a queue which enables O(1) access to the head and tail, as well as O(1) 
removal (given a reference to the node being removed)

A python dictionary maintains key-value pairs where the values point to nodes in the linked list.

When an existing value is accessed via get:

1. The reference to its node is looked up in the dictionary: O(1)
1. The node is promoted to the head (most-recently-used position) of the queue in an O(1) operation made possible by the 
   references maintained in the data structures.
  
When an item is set:

1. If the queue is at capacity, the item at the tail of the list (the least recently used item) is removed to make space. 
   This is O(1) because the doubly-linked-list maintains a reference to its tail
1. The item is considered *used* and is set as the head of the list (the position representing the most recently used item).
   This is also O(1) because the doubly-linked-list maintaines a reference to its head

