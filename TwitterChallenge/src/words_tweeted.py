# calculates the total number of times each word has been tweeted, and sorts them by ASCII
#WordCount
import os
path1 = 'tweet_input'
path2 = 'tweet_output'
InputFileName = "tweets.txt"
OutputFileName = "ft1.txt"

words = {}

def wordcount():
    os.chdir('..')
    os.chdir(path1)
    readfile = open(InputFileName, "r")
    for tweet in readfile:
        tweet = tweet.strip().split()
        for word in tweet:
            if word not in words:
                words[word] = 1
            elif word in words:
                words[word] = words[word] + 1
    readfile.close()

    os.chdir('..')
    os.chdir(path2)
    for key in sorted(words): #write words and values to output, sorted
        writefile.write("%s\t\t%s\n" %(key , words[key]))
    writefile.close()

if __name__ == '__main__':
    os.chdir('..')
    os.chdir(path2)
    writefile = open(OutputFileName, "w")
    wordcount()
