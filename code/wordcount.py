#WordCount
import os

if __name__ == '__main__':
    path1 = 'InsightData/wc_input'
    path2 = 'InsightData/wc_output'
    listing = os.listdir(path1)

    words = {} #initialize words dictionary

    os.chdir(path2) #write result txt in correct location
    writefile = open("wc_result.txt", "w")

    for infile in sorted(listing): #loop through input files
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
