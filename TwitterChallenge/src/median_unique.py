# Running Median
# calculates the running median number of unique words per tweet, by organizing tweet numbers into two heaps.
import os
Input_Path = 'tweet_input'
Output_Path = 'tweet_output'
Input_File_Name = "tweets.txt"
Output_File_Name = "ft.2.txt"

MaxHeap = [] #every key <= to current median
MinHeap = [] #every key >= to current median
RunningMedian = [] #initialize list of running medians

def SwapIfGreater(parentIndex, childIndex, heap): #Swaps parent and child indexes in heap if greater
    if heap[parentIndex] < heap[childIndex]:
        heap[parentIndex], heap[childIndex] = heap[childIndex], heap[parentIndex]

def greaterIndex(index1,index2, heap):
    if heap[index1] > heap[index2]:
        return index1
    else: #if index2's value is greater or equal to index1's value, return index2
        return index2

def sift(parentIndex, unsortedLen, heap):
    if unsortedLen == 2:
        SwapIfGreater(parentIndex, 1, heap)
    
    while parentIndex*2+2 < unsortedLen:
        leftChildIndex = parentIndex*2+1
        rightChildIndex = parentIndex*2+2

        greaterChildIndex = greaterIndex(leftChildIndex, rightChildIndex, heap)
        SwapIfGreater(parentIndex, greaterChildIndex, heap)
        parentIndex = greaterChildIndex

def AddToMinHeap(x): #storing MinHeap as MaxHeap internally to utilize same sift function
    global MinHeap
    MinHeap = [x*-1] + MinHeap
    sift(0, len(MinHeap), MinHeap)

def AddToMaxHeap(x):
    global MaxHeap
    MaxHeap = [x] + MaxHeap
    sift(0, len(MaxHeap), MaxHeap)

def RebalanceHeaps():
    global MaxHeap
    global MinHeap
    if (len(MaxHeap) - len(MinHeap)) > 1: #if MaxHeap is longer, add to MinHeap
        AddToMinHeap(MaxHeap[0])
        MaxHeap = MaxHeap[1:]
        sift(0, len(MaxHeap), MaxHeap)
    elif (len(MinHeap) - len(MaxHeap)) > 1: #if MinHeap is longer, add to MaxHeap
        AddToMaxHeap(MinHeap[0])
        MinHeap = MinHeap[1:]
        sift(0, len(MinHeap), MinHeap)

def FindMedian():
    if (len(MaxHeap) == 0 & len(MinHeap) == 0): #returns an invalid median if Heaps are empty
        return -1
    elif len(MinHeap) > len(MaxHeap):
        return float(MinHeap[0]*-1)
    elif len(MaxHeap) > len(MinHeap):
        return float(MaxHeap[0])
    else: #even number of elements
        return float((MaxHeap[0] + (MinHeap[0]*-1))/ 2.00)
                     
def MainMedian():
    os.chdir("..")
    os.chdir(Input_Path)
    readfile = open(Input_File_Name, "r")
    for line in readfile: #loop through each line/tweet in input file
        words = line.strip().split()
        currentmedian = FindMedian()
        if currentmedian == -1: #if heaps are empty, add to MaxHeap
            AddToMaxHeap(len(words))
        elif len(words) < currentmedian: #if the value is less than the current median
            AddToMaxHeap(len(words)) #Add to MaxHeap and rebalance
            RebalanceHeaps()
        elif len(words) > currentmedian: #if the value is greater than the current median
            AddToMinHeap(len(words)) #Add to MinHeap and rebalance
            RebalanceHeaps()
        elif len(words) == currentmedian: #if the value is equal to the current median
            if len(MaxHeap) > len(MinHeap): #add to the MinHeap if MaxHeap is greater
                AddToMinHeap(len(words))
                RebalanceHeaps()
            else:
                AddToMaxHeap(len(words)) #otherwise, add to the MaxHeap
                RebalanceHeaps()
        currentmedian = FindMedian()
        RunningMedian.append(currentmedian) #add current median to running median list
    readfile.close()

    for medians in RunningMedian:
        writefile.write("%s\n" %(medians))
    writefile.close()
    
if __name__ == '__main__':
    os.chdir("..")
    os.chdir(Output_Path) #write output file in correct location
    writefile = open(Output_File_Name, "w")
    MainMedian()