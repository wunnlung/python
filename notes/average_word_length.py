def main():
    x = []
    wordcount = 0
    totalcount = 0
    sentcount = 0
    
    inputfile = open("collosus.txt", "r")
    for line in inputfile:
        x = x + line.split()
    totalcount = totalcount + len(x)  
    print(totalcount)
            
    for i in x:
        wordcount = wordcount + 1
        for n in i:
            if n == "." or n == "!" or n == "?":
                print("this sentence has", wordcount, "words")
                wordcount = 0
                sentcount = sentcount + 1
    print("the average sentence length is", totalcount/sentcount)

main()


def input():
    inputfile = open("collosus.txt", "r")
    wordCount = 0
    sentCount = 0
    for line in inputfile:
        wordList = line.split()
        wordCount = wordCount + len(wordList)

        print(wordList)
        for word in wordList:
            if word[-1] == "." or word[-1] == "!" or word[-1] == "?":
                sentCount = sentCount + 1
    print(sentCount)
    print(wordCount)
    print("avg words:", wordCount/sentCount)

input()
