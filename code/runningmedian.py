#Running Median
import os
import heapq

if __name__ == '__main__':
    path1 = 'InsightData/input'
    path2 = 'InsightData/output'
    listing = os.listdir(path1)
    
    linesprocessed = 0 #initialize lines processed counter
    MaxHeap = [] #every key <= to current median
    MinHeap = [] #every key >= to current median
 
    
    os.chdir(path2) #write output file in correct location
    writefile = open("med_result.txt", "w")

def RebalanceHeap():
    if (len(MaxHeap) - len(MinHeap)) > 1:
        heapq.heappush(MinHeap, max(MaxHeap))
        max(MaxHeap) = MaxHeap[-1]
        MaxHeap.pop()
        heapify(MaxHeap)
    elif (len(MinHeap) - len(MaxHeap)) > 1:
        heapq.heappush(MaxHeap, min(MinHeap))
        min(MinHeap) = MinHeap[-1]
        MinHeap.pop()
        heapq.heapify(MinHeap)

def findmedian():
    if len(MaxHeap) + len(MinHeap) == 0:
        return 0
    elif len(MinHeap) > len(MaxHeap):
        return MinHeap[0]
    elif len(MaxHeap) > len(MinHeap):
        return MaxHeap[0]
    elif len(MinHeap) == len(MaxHeap):
        return ((MaxHeap[0] + MinHeap[0])/ 2.0)


for infile in listing: #loop through each input file
    os.chdir(path1)
    readfile = open("%s" %(infile), "r")
    
    for line in iter(readfile): #loop through each line in input file
        line = line.strip().replace("-", " ").split(" ")
            currentmedian = findmedian()
            if len(line) < currentmedian:
                heapq.heappush(MaxHeap, len(line))
                RebalanceHeap()
            elif len(line) > currentmedian:
                heapq.heappush(MinHeap, len(line))
                RebalanceHeap()
            elif len(line) == currentmedian:
                if len(MaxHeap) > len(MinHeap):
                    heapq.heappush(MinHeap, len(line))
                    RebalanceHeap()
                elif len(MaxHeap) < len(MinHeap):
                    heapq.heappush(MaxHeap, len(line))
                    RebalanceHeap()
                elif len(MaxHeap) == len(MinHeap):
                    heapq.heappush(MaxHeap, len(line))
                    RebalanceHeap()
    readfile.close()

currentmedian = findmedian()
writefile.write("The running median words per line is %s!" %(currentmedian))

writefile.close()
