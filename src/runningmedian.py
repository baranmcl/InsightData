#Running Median

readfile = open("constantsorrow.txt", "r")
writefile = open("output.txt", "w")

WordsPerLine = []

def median(lst):
    lst = sorted(lst)
    if len(lst) < 1:
        return None
    elif len(lst) % 2 == 1:
        return lst[((len(lst)+1)/2)-1]
    elif len(lst) % 2 == 0:
        return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

for line in iter(readfile):
    line = line.strip().split()
    WordsPerLine.append(len(line))

runningmedian = median(WordsPerLine)
writefile.write("The Running Median Words Per Line is %s" %(runningmedian))

readfile.close()
writefile.close()
