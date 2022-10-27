bidenfile = open("biden20dnc.txt", "r")
trumpfile = open("trump20rnc.txt", "r")


x = input("what word do you wanna search?: ")

def biden():
    bidenfile = open("biden20dnc.txt", "r")
    wordCount = 0
    econCount = 0
    econCount2 = 0
    bidenstring = bidenfile.read()
    bidensplit = bidenstring.split()
    bidenlist = []
    sentCount = 0
    for i in bidensplit:
        bidenlist.append(i.lower())
        #bidenstring = bidenstring + i.lower()
    #for word in bidenlist:
        #print(word)
    econCount = bidenlist.count(x) + bidenlist.count(x + ",") + bidenlist.count(x + ".") + bidenlist.count(x + "'s") + bidenlist.count(x + "s.") + bidenlist.count(x + ":")
    econCount2 = bidenstring.count(x)

    for i in bidenlist:
        for n in i:
            if n == "." or n == "!" or n == "?":
                sentCount = sentCount + 1

    bidenfile = open("biden20dnc.txt", "r")
    for line in bidenfile:
        wordList = line.split()
        wordCount = wordCount + len(wordList)
        words = line.split()
        
                
    #print(econCount)     
    print(wordCount) #3346 words long
    print(econCount2)
    print("the average sentence length is", wordCount/sentCount)

#biden()

print("")

def trump():
    trumpfile = open("trump20rnc.txt", "r")
    wordCount = 0
    econCount = 0
    sentCount = 0
    trumpstring = trumpfile.read()
    trumpsplit = trumpstring.split()
    trumplist = []
    for i in trumpsplit:
        trumplist.append(i.lower())

    
    econCount = trumplist.count(x) + trumplist.count(x + ",") + trumplist.count(x + ".") + trumplist.count(x + "'s") + trumplist.count(x + "s.") + trumplist.count(x + ":")

    trumpfile = open("trump20rnc.txt", "r")
    for line in trumpfile:
        wordList = line.split()
        wordCount = wordCount + len(wordList)
        words = line.split()

    for i in trumplist:
        for n in i:
            if n == "." or n == "!" or n == "?":
                sentCount = sentCount + 1
                
    #print(econCount)     
    print(wordCount) #5714 words long
    print(econCount)
    print("the average sentence length is", wordCount/sentCount)

#trump()


def main():
    outputfile = open("lab3output.txt","w")
    outputfile.write("hehehe haw\ngrrrrr")
    outputfile.close()

#main()


def tickets():
    x = int(input("whats ur age?: "))
    if x <= 3:
        print("ur ticket is free!!")
    elif x <= 18:
        print("ur ticket is half off!!!")
    elif x <= 60:
        print("haha sorry u have to buy a normal ticket!!!")
    else:
        print("ur old so u get a ticket for 3/4ths the price")

#tickets()

def listmovies():
    print("movie 1: pirates of the carribean\nmovie 2: joe mama")

def tickets2():
    print("(A) List Movies:")
    print("(B) Determine Ticket Price")
    x = input("What would you like to do?: ")
    if x.upper() == "A":
        print("movie 1: pirates of the carribean\nmovie 2: joe mama")
    elif x.upper() == "B":
        y = int(input("whats ur age?: "))
        if y <= 3:
            print("ur ticket is free!!")
        elif y <= 18:
            print("ur ticket is half off!!!")
        elif y <= 60:
            print("haha sorry u have to buy a normal ticket!!!")
        else:
            print("ur old so u get a ticket for 3/4ths the price")
    else:
        print("thats not one of the options you dummy")

#tickets2()

def ticketmain():
    print("(A) List Movies:")
    print("(B) Determine Ticket Price")
    x = input("What would you like to do?: ")
    if x.upper() == "A":
        listmovies()
    elif x.upper() == "B":
        tickets()

ticketmain()
