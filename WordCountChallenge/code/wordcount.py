#WordCount
import os
path1 = '/Users/baranmcl/Desktop/codes/python_projects/insight/input'
path2 = '/Users/baranmcl/Desktop/codes/python_projects/insight/output'
listing = os.listdir(path1)

words = {}

def wordcount(x):
    for infile in sorted(x): #loop through input files
        os.chdir(path1)
        readfile = open("%s" %(infile), "r")
        for word in readfile.read().lower().strip().replace("-", " ").split(): #loop through each word in input files, making all words lowercase and replacing hyphens
            for char in word: #remove unwanted punctuation
                if char in '()!,?.;:"/\<>&^%$#@~`':
                    char = ""
            if word not in words:
                words[word] = 1
            elif word in words:
                    words[word] = words[word] + 1
        readfile.close()

    os.chdir(path2)
    for key in sorted(words): #write words and values to output
        writefile.write("%s\t\t%s\n" %(key , words[key]))
    writefile.close()

if __name__ == '__main__':
    os.chdir(path2)
    writefile = open("wc_result.txt", "w")
    wordcount(listing)
