#Todd Shriber, Comp Sci 101
#Project 2, due on Feb 22 2022

import time
#using this for better user interface (delay between strings so the user isnt flooded with massive text blocks)

#Just a note, func C takes a while to load just because of the sheer length of the text documents I use
#so it works but it just takes a minute

#gonna split it into four different functions. I'll start with main that will call the other three when neccessary
def main():
    print("Welcome to Todd's Library!\n")
    time.sleep(1)
    print("A. Calculate average word length of a book/document.\
\nB. Total count of a single word in a book?\
\nC. Comparing French and English books")
    x = input("Which operation would you like to perform?:\n")
    if x.lower() == "a": #make it x.lower in case they pick
        #"A" instead of "a", because it wouldn't count it otherwise
        A()
    elif x.lower() == "b":
        B()
    elif x.lower() == "c":
        C()
    else: #just in case the person selects something that isn't a normal pick.
        print("\n hey dude that isn't a valid input\n")
        main() #this will make it loop back through until the user gives a valid input




#looking back, I thought of some better ways to format it,
#so there would be much less copy pasting, but I already started this way and
#it would be a pain to change something that already works



def A():
    print("\nOption A: calculating the average word length of a book\n")
    print("Book List:\n1. The Stuff of Manhood\
\n2. Les Huit Jours du Petit Marquis & Carlos et Cornélius (French)\
\n3. Forest Scenes in Norway and Sweeden")
    x = int(input("Which book would you like to select?:\n"))
    #just the same method demonstrated in the main function
    print("\nLoading...") #illustrates a little loading feature
    time.sleep(3) #will take 3 seconds to "load" the results
#book 1
    if x == 1:
        print("\nBook 1: The Stuff of Manhood")
        book = open("thestuff.txt", "r") #open the specific book
        bookString = book.read()
        words = bookString.split()
        average = sum(len(word) for word in words) / len(words) #credit to stack overflow for this line of text
        print("the average word length for this book is", average)
        time.sleep(2)
        y = input("\nWould you like to select another book?\nA. Yes\nB. No\n")
        #if yes is selected it will loop back around to pick another book
        if y.lower() == "a" or y.lower() == "yes":
            A()
        else:
            print("\nThank you for visiting Todd's library!") # if not it will end the code
#book 2
    elif x == 2: #all I am doing here is copying and pasting the same code for this book
        print("\nBook 2: Les Huit Jours du Petit Marquis & Carlos et Cornélius (French)") 
        book = open("les_huit.txt", "r")
        #the only difference between the three is I change what book is opened each time
        bookString = book.read()
        words = bookString.split()
        average = sum(len(word) for word in words) / len(words) 
        print("the average word length for this book is", average)
        time.sleep(2)
        y = input("\nWould you like to select another book?\nA. Yes\nB. No\n") 
        if y.lower() == "a" or y.lower() == "yes":
            A()
        else:
            print("\nThank you for visiting Todd's library!") 
#book 3
    elif x == 3:
        print("\nBook 3: Forest Scenes in Norway and Sweeden") 
        book = open("forest_scenes.txt", "r") 
        bookString = book.read()
        words = bookString.split()
        average = sum(len(word) for word in words) / len(words) 
        print("the average word length for this book is", average)
        time.sleep(2)
        y = input("\nWould you like to select another book?\nA. Yes\nB. No\n") 
        if y.lower() == "a" or y.lower() == "yes":
            A()
        else:
            print("\nThank you for visiting Todd's library!") 
#invalid book
    else:
        print("\n sorry, there are no records for that book\n")
        A() #if the input is not an integer, it will return an error.
        #Tried a couple workarounds but none worked. I could have it 






#honesty most of this stuff is just copied and pasted from def A.
#Because all of the book picking stuff is all the same
def B(): 
    print("\nBook List:\n1. The Stuff of Manhood\n2. \
Les Huit Jours du Petit Marquis & Carlos et Cornélius (French)\
\n3. Forest Scenes in Norway and Sweeden")
    x = int(input("Which book would you like to select?:\n"))
    word = input("\nWhat is the word you would like to look for?:\n")
    print("\nLoading...")
    time.sleep(3)
#book 1
    if x == 1:
        print("\nBook 1: The Stuff of Manhood")
        book = open("thestuff.txt", "r") 
        bookRead = book.read()
        bookSplit = bookRead.split() #all of this code I wrote previously for lab3. 
        bookArray = []
        for i in bookSplit:
            bookArray.append(i.lower())
            #this will create a list of every word in the book, which I can
            #then count for user specified word right below
        wordCount = bookArray.count(word) + bookArray.count(word + ",") + \
                    bookArray.count(word + ",") + bookArray.count(word + "s") + \
                    bookArray.count(word + "s.")
        print("your word appears", wordCount, "times in this book")
        time.sleep(2)
        y = input("\nWould you like to pick another word/book?\nA. Yes\nB. No\n")
        #if yes is selected it will loop back around to pick another book
        if y.lower() == "a" or y.lower() == "yes":
            B()
        else:
            print("\nThank you for visiting Todd's library!") # if not it will end the code
#book 2
    elif x == 2: 
        print("\nBook 2: Les Huit Jours du Petit Marquis & Carlos et Cornélius (French)") 
        book = open("les_huit.txt", "r") 
        bookRead = book.read()
        bookSplit = bookRead.split() #all of this code I wrote previously for lab3. 
        bookArray = []
        for i in bookSplit:
            bookArray.append(i.lower()) 
        wordCount = bookArray.count(word) + bookArray.count(word + ",") + \
                    bookArray.count(word + ",") + bookArray.count(word + "s") + \
                    bookArray.count(word + "s.")
        print("your word appears", wordCount, "times in this book")
        time.sleep(2)
        y = input("\nWould you like to pick another word/book?\nA. Yes\nB. No\n")
        #if yes is selected it will loop back around to pick another book
        if y.lower() == "a" or y.lower() == "yes":
            B()
        else:
            print("\nThank you for visiting Todd's library!")
#book 3
    elif x == 3:
        print("\nBook 3: Forest Scenes in Norway and Sweeden")
        book = open("forest_scenes.txt", "r") 
        bookRead = book.read()
        bookSplit = bookRead.split() 
        bookArray = []
        for i in bookSplit:
            bookArray.append(i.lower())
        
        wordCount = bookArray.count(word) + bookArray.count(word + ",") + \
                    bookArray.count(word + ",") + bookArray.count(word + "s") + \
                    bookArray.count(word + "s.")
        print("your word appears", wordCount, "times in this book")
        time.sleep(2)
        y = input("\nWould you like to pick another word/book?\nA. Yes\nB. No\n") 
        if y.lower() == "a" or y.lower() == "yes":
            B()
        else:
            print("\nThank you for visiting Todd's library!")
#invalid book
    else:
        print("\n sorry, there are no records for that book\n")
        B() #will loop back to func B again if user chooses a nonexitent book


def C():
    print("\nOption C: comparing English and French!")
    print("\nEnglish book: Forest Scenes in Norway and Sweeden\
\nFrench book: Les Huit Jours du Petit Marquis & Carlos et Cornélius")
    time.sleep(1)
    x = int(input("\n1. average sentence length\n2. punctuation (', -,) to word ratio\n"))
#average sentence length
    if x == 1:
        #this is the code I created to calculate average sentence length
        #I think it works better than the class code, as it checks
        #every single letter and not just the last letter of a word.
        #this is important because a word could have a " at the end of it, which is after the .
        english = open("forest_scenes.txt", "r")
        french = open("les_huit.txt", "r")
        bookCount = 0
        x = [english,french] #decided to have it loop through the two different books, as to save space
        for inputFile in x: #less copy pasting
            #this line is important for telling what book we are listing
            bookCount = bookCount + 1
            
            wordCount = 0
            sentcount = 0
            wordList = []
            words = []

            if bookCount == 1: 
                print("\nloading...\n Ok this one actually is loading and not me making \
it look like it is loading")
                print(" On my computer it took about a minute to load")
            else:
                print("\nloading...")

            for line in inputFile:
                wordList = line.split()
                words = words + line.split() #this one line is making the entire thing lag
                #because the books are so big it takes a very long time to load
                #i was testing things out for an entire hour because i thought it was an error
                #tunrs out it was correct code but it took like 2 minutes to load on my computer
                #very sorry if it seems like it doesn't work. It works, it just takes a while. Very sorry
                wordCount = wordCount + len(wordList)
            #print(wordCount)
            for i in words:
                for n in i:
                    if n == "." or n == "!" or n == "?":
                        sentcount = sentcount + 1
    
            if bookCount == 1: #call back to the book count (English vs. French)
                print("\nthe average sentence length for the English book is", wordCount/sentcount)
            elif bookCount == 2:
                print("\nthe average sentence length for the French book is", wordCount/sentcount)

        time.sleep(2)
        y = input("\nWould you like to select another function?\nA. Yes\nB. No\n") 
        if y.lower() == "a" or y.lower() == "yes":
            C()
        else:
            print("\nThank you for visiting Todd's library!")
#symbols
    elif x == 2:
        #This first bit is just copy pasted from right above
        english = open("forest_scenes.txt", "r")
        french = open("les_huit.txt", "r")
        bookCount = 0
        x = [english,french] 
        for inputFile in x: 
            bookCount = bookCount + 1
            
            read = inputFile.read()
            List = read.split()
            totalWords = len(List)
           # print(totalWords)

            bookArray = []
            symbolCount = 0
            ActualSC = 0
            for i in read:
                bookArray.append(i.lower())
            for i in bookArray:
                for n in i:
                    if n == "-" or n == "'":
                        symbolCount += 1 #this is something I just remembered from swift
                        #I am very suprised to see it actually works
            if bookCount == 1:
                print("\nFor the English book, there were", totalWords, "total words, and", symbolCount, "\
symbols.\nThis means that the symbol to word ratio was", symbolCount/totalWords)
            elif bookCount ==2:
                print("\nFor the French book, there were", totalWords, "total words, and", symbolCount, "\
symbols.\nThis means that the symbol to word ratio was", symbolCount/totalWords)
        y = input("\nWould you like to select another function?\nA. Yes\nB. No\n") 

        time.sleep(2)
        if y.lower() == "a" or y.lower() == "yes":
            C()
        else:
            print("\nThank you for visiting Todd's library!")
#invalid input           
    else:
        print("\n sorry, Todd's library can't handle that function yet\n")
        C() #loops back to func C again if invalid input
    


main()
