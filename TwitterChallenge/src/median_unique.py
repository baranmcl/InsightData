# calculates the median number of unique words per tweet
#Running Median
import os
import heapq

path1 = 'InsightData/tweet_input'
path2 = 'InsightData/tweet_output'
listing = os.listdir(path1)

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

def mainmedian(x):
    for infile in sorted(x): #loop through each input file
        os.chdir(path1)
        readfile = open("%s" %(infile), "r")
        
        for line in iter(readfile): #loop through each line in input file
            line = line.strip().replace("-", " ").split(" ")
            
            currentmedian = findmedian()
            if currentmedian != 0:
                runningmedian.append(currentmedian)
            
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
    runningmedian.append(currentmedian)
    
    for medians in runningmedian:
        writefile.write("%s\n" %(medians))

    writefile.close()


if __name__ == '__main__':
    
    os.chdir(path2) #write output file in correct location
    writefile = open("med_result.txt", "w")
    
    mainmedian(listing)
