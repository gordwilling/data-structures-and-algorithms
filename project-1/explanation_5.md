# Udacity - Data Structures and Algorithms - Project 1

## Problem 5 - Block Chain

A block chain is a list wherein each element contains a hash that is dependent on all of the previous
blocks in the chain. Validating this hash involves recalculating the hash for each block in the entire
list, and as such proves (practically) that the chain has not been tampered with.

Adding a block to the chain involves:

1. The hash value of the previous block is set in the new block
1. The hash for the new block is calculated
1. The new block is appended to the list of blocks

Tamper proofing comes from the previous hash being used in the new hash calculation

Hash calculation involves applying a mathematical formula to each element of the input, making it linearly dependent 
on the input length, so O(n) time complexity and constant O(1) space complexity.

