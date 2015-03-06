#WordCount
import os

path1 = '/Users/baranmcl/Desktop/python_projects/insight/input'
path2 = '/Users/baranmcl/Desktop/python_projects/insight/output'
listing = os.listdir(path1)

words = {}

os.chdir(path2)
writefile = open("wc_result.txt", "w")

for infile in listing:
    os.chdir(path1)
    readfile = open("%s" %(infile), "r")
    for word in readfile.read().split():
        if word not in words:
            words[word] = 1
        if word in words:
            words[word] = words[word] + 1
    for key in words.keys():
        os.chdir(path2)
        writefile.write("%s\t\t%s\n" %(key , words[key]))

    readfile.close()
writefile.close()
