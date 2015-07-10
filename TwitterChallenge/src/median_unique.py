# calculates the median number of unique words per tweet
#Running Median
import os
import heapq

path1 = 'tweet_input'
path2 = 'tweet_output'
InputFileName = "tweets.txt"

MaxHeap = [] #every key <= to current median
MinHeap = [] #every key >= to current median
    
runningmedian = [] #initialize list of running medians

def RebalanceHeap():
    if (len(MaxHeap) - len(MinHeap)) > 1:
        heapq.heappush(MinHeap, max(MaxHeap))
        MaxHeap.remove((max(MaxHeap)))
        heapq.heapify(MaxHeap)
    elif (len(MinHeap) - len(MaxHeap)) > 1:
        heapq.heappush(MaxHeap, min(MinHeap))
        MinHeap.remove((min(MinHeap)))
        heapq.heapify(MinHeap)

def findmedian():
    if len(MaxHeap) + len(MinHeap) == 0:
        return 0
    elif len(MinHeap) > len(MaxHeap):
        return float(MinHeap[0])
    elif len(MaxHeap) > len(MinHeap):
        return float(max(MaxHeap))
    elif len(MinHeap) == len(MaxHeap):
        return float((max(MaxHeap) + MinHeap[0])/ 2.0)

def mainmedian():
    os.chdir("..")
    os.chdir(path1)
    readfile = open(InputFileName, "r")
    for line in readfile: #loop through each line/tweet in input file
        words = line.strip().split()
        currentmedian = findmedian()
        if currentmedian != 0:
            runningmedian.append(currentmedian)
        if len(words) < currentmedian:
            heapq.heappush(MaxHeap, len(words))
            RebalanceHeap()
        elif len(words) > currentmedian:
            heapq.heappush(MinHeap, len(words))
            RebalanceHeap()
        elif len(words) == currentmedian:
            if len(MaxHeap) > len(MinHeap):
                heapq.heappush(MinHeap, len(words))
                RebalanceHeap()
            elif len(MaxHeap) < len(MinHeap):
                heapq.heappush(MaxHeap, len(words))
                RebalanceHeap()
            elif len(MaxHeap) == len(MinHeap):
                heapq.heappush(MaxHeap, len(words))
                RebalanceHeap()
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
