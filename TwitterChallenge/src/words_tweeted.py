# Word Count
# calculates the total number of times each word has been tweeted, and sorts them by ASCII
import os
Input_Path = 'tweet_input'
Output_Path = 'tweet_output'
Input_File_Name = "tweets.txt"
Output_File_Name = "ft1.txt"

words = {} #initialize hash table of words and counts

def wordcount():
    os.chdir('..')
    os.chdir(Input_Path)
    readfile = open(Input_File_Name, "r")
    for tweet in readfile:
        tweet = tweet.strip().split()
        for word in tweet:
            if word not in words:
                words[word] = 1
            elif word in words:
                words[word] = words[word] + 1
    readfile.close()

    os.chdir('..')
    os.chdir(Output_Path)
    for key in sorted(words): #write words and values to output, sorted
        writefile.write("%s\t\t%s\n" %(key , words[key]))
    writefile.close()

if __name__ == '__main__':
    os.chdir('..')
    os.chdir(Output_Path)
    writefile = open(Output_File_Name, "w")
    wordcount()
