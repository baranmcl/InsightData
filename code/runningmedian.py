#Running Median
import os

path1 = '/Users/baranmcl/Desktop/python_projects/insight/input'
path2 = '/Users/baranmcl/Desktop/python_projects/insight/output'
listing = os.listdir(path1)

WordsPerLine = []
runningmedian = 0

os.chdir(path2)
writefile = open("med_result.txt", "w")

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
        return None
    elif len(lst) % 2 == 1:
        return lst[((len(lst)+1)/2)-1]
    elif len(lst) % 2 == 0:
        return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

for infile in listing:
    os.chdir(path1)
    readfile = open("%s" %(infile), "r")
    for line in iter(readfile):
        line = line.strip().split()
        WordsPerLine.append(len(line))
    readfile.close()

runningmedian = median(WordsPerLine)
writefile.write("The Running Median Words Per Line is %s!" %(runningmedian))

writefile.close()
