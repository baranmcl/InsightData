# calculates the total number of times each word has been tweeted, and sorts them by ASCII
#WordCount
import os
path1 = 'TwitterChallenge/tweet_input'
path2 = 'TwitterChallenge/tweet_output'
listing = os.listdir(path1)

words = {}

def wordcount(x):
    os.chdir(path1)
    readfile = open("tweets.txt", "r")
    for word in readfile:
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
    writefile = open("ft1.txt", "w")
    wordcount(listing)
