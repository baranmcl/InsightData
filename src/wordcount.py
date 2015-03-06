#WordCount

readfile = open("constantsorrow.txt", "r")
writefile = open("output.txt", "w")

words = {}

for word in readfile.read().split():
	if word not in words:
		words[word] = 1
	if word in words:
		words[word] = words[word] + 1


for key in words.keys():
	writefile.write("%s\t\t%s\n" %(key , words[key]))


readfile.close()
writefile.close()
