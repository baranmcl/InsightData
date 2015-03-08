#Running Median
import os

if __name__ == '__main__':
    path1 = 'InsightData/input'
    path2 = 'InsightData/output'
    listing = os.listdir(path1)
    
    linesprocessed = 0 #initialize lines processed counter
    MaxHeap = [] #initialize heaps
    MinHeap = []
    MaxLength = len(MaxHeap)
    MinLength = len(MinHeap)
    
    os.chdir(path2) #write output file in correct location
    writefile = open("med_result.txt", "w")

def findmedian(x, y):
    if (len(x)+len(y)) % 2 == 0:
        median = (min(x) + max(y)) / 2.0 #median is average of two middle-most numbers
        return median
    elif (len(x)+len(y)) % 2 == 1: #if the number of lines is odd, median is in the middle
        if len(x) > len(y):
            return min(x)
        elif len(x) < len(y):
            return max(y)


for infile in listing: #loop through each input file
    os.chdir(path1)
    readfile = open("%s" %(infile), "r")
    
    for line in iter(readfile): #loop through each line in input file
        line = line.strip().split()
        
        if linesprocessed >= 2: #rebalance heaps
            if (MaxLength - MinLength) > 1:
                MinHeap.append(max(MaxHeap))
                MaxHeap.remove(max(MaxHeap))
            elif (MinLength - MaxLength) > 1:
                MaxHeap.append(min(MinHeap))
                MinHeap.remove(min(MinHeap))

        if linesprocessed == 0: #calculate current median
            currentmedian = 0
        elif linesprocessed == 1:
            currentmedian = MaxHeap[0]
        else:
            currentmedian = findmedian(MaxHeap, MinHeap) #calculate current running median

        if len(line) > currentmedian: #place line word count in appropriate heap
            MaxHeap.append(len(line))
        elif len(line) < currentmedian:
            MinHeap.append(len(line))
        elif len(line) == currentmedian:
            if MaxLength > MinLength:
                MinHeap.append(len(line))
            else:
                MaxHeap.append(len(line))
        linesprocessed = linesprocessed + 1
    readfile.close()
    
if linesprocessed >= 2: #rebalance heaps for final median calculation
    if (MaxLength - MinLength) > 1:
        MinHeap.append(max(MaxHeap))
        MaxHeap.remove(max(MaxHeap))
    elif (MaxLength - MinLength) > 1:
        MaxHeap.append(min(MinHeap))
        MinHeap.remove(min(MinHeap))

currentmedian = findmedian(MaxHeap, MinHeap) #calculate final median

writefile.write("The Running Median Words Per Line is %s!" %(currentmedian))

writefile.close()
