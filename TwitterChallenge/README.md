##Insight Data Science Code Challenge

#Objectives

1. Calculated the total number of times each word has been tweeted.
2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in.

#Explanation

1. Accomplished by looping through each unique word in every tweet (separated by whitespace), and indexing them in a hash table. This hash table is then sorted and written to the output document. The worst-case scenario run-time for this code is O(n*log(n)).

2. Accomplished by looping through each tweet and calculating how many words are in each tweet. This number is then stored in a Binary Heap structure - either a MaxHeap or a MinHeap. The MaxHeap has each node less than or equal to its root, while the MinHeap has each node greater than or equal to its root. As numbers are added, the heaps are rebalanced. The running median is calculated from the roots of the heaps. The worst-case scenario run-time for this code is O(n*log(n)).