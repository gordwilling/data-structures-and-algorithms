# Udacity - Data Structures and Algorithms - Project 1

## Problem 1 - LRU Cache

The LRU cache provides get and set operations with O(1) time complexity and O(n) space complexity.

Key-value pairs can be stored in a python Dictionary which meets these complexity requirements. Key values are
also stored in a Queue, which provides O(1) time access to the first and last elements in the collection. When the
cache is accessed (via get or set):

1. If the queue is full, the item at the front of the queue (the least recently used item) is removed to make space
1. The key is considered *used* and added to the end of the queue (the position representing the most recently used item)
1. The value is either inserted into or retrieved from the cache.
