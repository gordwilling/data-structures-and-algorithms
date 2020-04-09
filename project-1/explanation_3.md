# Udacity - Data Structures and Algorithms - Project 1

## Problem 3 - Huffman Coding


### Procedure 
Huffman Coding involves 3 steps:

1. Generate the Huffman encoding scheme for the input data
1. Create a lookup table mapping each datum to its encoding
1. Encode the data using the lookup table

Huffman encoding must produce two outputs:

1. The encoded data
1. The Huffman tree, required to decode the data

### Time and space Complexity

1. Generating the Huffman encoding tree is an iterative process wherein:
    1. a collection of data is inserted into a priority queue: O(n)
    1. the priorty queue is used to give constant-time access to the two least frequence elements in the data
        1. The two least frequent elements are used to create a node in the Huffman tree
    1. The node is inserted into the priority queue, documented as O(logn) time complexity
    1. Steps ii and iii are repeated until there is only one node left in the queue (this is the root of the Huffman Tree)
    
 The number of elements inserted into the priority q is proportional to the amount of input, so time complexity for
 building the tree is O(logn)
 
 1. Encoding the data involves looking up the encoding in a map O(1), once for each element in the data, thus O(n) time complexity
 
 1. Decoding the data involves walking the tree for each character in the encoded data, which is a worst case O(logn) each time, so O(nlogn) in total
 
 As for space, both the tree and priority queue require n elements to be stored, so space complexity is O(n) 
 
   
 
    
    