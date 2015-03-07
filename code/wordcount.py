#WordCount
import os

if __name__ == '__main__':
    path1 = 'InsightData/wc_input' #set input and output paths
    path2 = 'InsightData/wc_output'
    listing = os.listdir(path1)

    words = {} #initialize words dictionary

    os.chdir(path2) #create result file
    writefile = open("wc_result.txt", "w")

for infile in listing: #loop through input files
    os.chdir(path1)
    readfile = open("%s" %(infile), "r")
    for word in readfile.read().split(): #loop through each word in input files
        if word not in words:
            words[word] = 1
        if word in words:
            words[word] = words[word] + 1
    for key in words.keys(): #write words and values to output
        os.chdir(path2)
        writefile.write("%s\t\t%s\n" %(key , words[key]))

    readfile.close()
writefile.close()
