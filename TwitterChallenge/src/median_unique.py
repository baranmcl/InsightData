# calculates the median number of unique words per tweet
#Running Median
import os

path1 = 'tweet_input'
path2 = 'tweet_output'
InputFileName = "tweets.txt"

MaxHeap = [] #every key <= to current median
MinHeap = [] #every key >= to current median

runningmedian = [] #initialize list of running medians

def swap_if_greater(pIndex, cIndex, heap):
    if heap[pIndex] < heap[cIndex]:
        heap[pIndex], heap[cIndex] = heap[cIndex], heap[pIndex]

def sift(pIndex, unsortedLen, heap):
    greaterIndex = lambda x, y: x if heap[x] > heap[y] else y
    while pIndex*2+2 < unsortedLen:
        LeftcIndex = pIndex*2+1
        RightcIndex = pIndex*2+2

        greater_child_index = greaterIndex(LeftcIndex, RightcIndex)
        
        swap_if_greater(pIndex, greater_child_index, heap)

        pIndex = greater_child_index

def Add_To_Min_Heap(x):
    MinHeap = [x*-1] + MinHeap
    sift(0, len(MinHeap), MinHeap)

def Add_To_Max_Heap(x):
    MaxHeap = [x] + MaxHeap
    sift(0, len(MaxHeap), MaxHeap)

def findmedian():
    if len(MaxHeap) + len(MinHeap) == 0:
        return "empty"
    elif len(MinHeap) > len(MaxHeap):
        return float(MinHeap[0]*-1)
    elif len(MaxHeap) > len(MinHeap):
        return float(MaxHeap[0])
    elif len(MinHeap) == len(MaxHeap):
        return float((MaxHeap[0] + (MinHeap[0]*-1)/ 2.00)

def mainmedian():
    os.chdir("..")
    os.chdir(path1)
    readfile = open(InputFileName, "r")
    for line in readfile: #loop through each line/tweet in input file
        words = line.strip().split()
        currentmedian = findmedian()
        if currentmedian == "empty":
            runningmedian.append(len(words))
        elif len(words) < currentmedian:
            Add_To_Max_Heap(len(words))
        elif len(words) > currentmedian:
            Add_To_Min_Heap(len(words))
        elif len(words) == currentmedian:
            if len(MaxHeap) > len(MinHeap):
                Add_To_Min_Heap(len(words))
            else:
                Add_To_Max_Heap(len(words))
                     
    readfile.close()
    
    currentmedian = findmedian()
    runningmedian.append(currentmedian)
    
    for medians in runningmedian:
        writefile.write("%s\n" %(medians))
    writefile.close()
    
if __name__ == '__main__':
    os.chdir("..")
    os.chdir(path2) #write output file in correct location
    writefile = open("ft2.txt", "w")
    mainmedian()