#Todd Shriber, Comp Sci, 3/29/2022
#
#Quick note, I did try my best to incorporate
#a few lines of text into graphics.py to allow
#me to rotate the text boxes, however nothing
#I tried worked. I was thinking of importing
#turtle.py through pip, but then you
#wouldn't be able to test it!
#
#what my code does is it takes a set text file,
#and turns it into a Word Cloud, with the size
#being determined by how many times one word appears
#only problem is that if too many distinct words are
#put in, the python module will get stuck in an indefinite
#while loop, and it will stop working.
#for testing purposes, I have supplied a .txt file
#of the lyrics for Twenty One Pilots House of Gold
#
#the system i used for collision to not happen is pretty
#simple. Pretty much, it generates random coordinates
#(for anywhere in the graphics window) and it runs
#and checks if the overlap with any previously accepted
#coordinates. If it doesn't overlap, then the coordinates
#are accepted, in which case it prints the new word with
#those coordinates, and adds them to a list of all the
#coordinates, so it can check again. The idea for how I
#completed this came from game design. I'm taking an
#online course on game design, and the first project was
#to recreate pong using Löve2D. It had each paddle as it's
#own box, and it constantly checked for colision, or if
#the ball and paddle hitboxes overlapped. I had to get a
#little creative here, however, because text boxes don't
#have set windows. Instead, they are printed at a single
#point, directly in the center of the words printed. So
#therefore, I estimated the general size of words, and said
#they were 70 pixels in the x length, and 50 in the y length
#However, if i chose to do so, I can easily change those numbers
#so the words can have more space in between, or less.
#the only problem presented in this method is that there
#is an indefinite maximum words that can be put in, depending
#on what I set the borders of the hitboxes to be. If its lower,
#then more words are allowed to appear, with less space in
#between each word. If the hitboxes are bigger, then
#less words can appear. Also, because placements are
#completely random for the entire window, there isn't a
#specific amount of words that cna fit into a set size.
#for example, you can run this code with the hitboxes being
#100x and 100y, and you might get about 11 words on the screen
#before it breaks. The next time you might get 12, or 10, or
#even 13. This is because it is random, so it doesn't know
#about space efficiency. Anyway, this is a really long comment,
#and I'll let you see the code now below.

from graphics import *
import random
import math
import time
#important for testing if file exists
import os.path

#decided to give 2 test options. text.txt is Twenty One Pilots,
#text2.txt is Peanut Butter Jelly Time
#comment one line out if you want to test one of them

#crating window 
win = GraphWin("Word Bubble Thing",800,800)
win.setBackground(color_rgb(214,222,133))

#starting entries
enter = Entry(Point(400,400),8)
enter.draw(win)
button = Rectangle(Point(300,500), Point(500,575))
button.setFill(color_rgb(82, 47, 30))
button.draw(win)
word = Text(Point(400,520), "Click to start")
word.draw(win)
message = Text(Point(400,380), "Enter text file here. Don't include the .txt")
message.draw(win)

mouse = win.getMouse()
message.undraw()

#doesn't start until click is inside button
entry = enter.getText()
testFile = os.path.exists(entry+".txt")

#first check if mouse button is accepted
while mouse.getX()>500 and mouse.getX()<300 and mouse.getY()<500 and mouse.getY()>575:
    mouse = win.getMouse()

#if mouse accepted, check if the file type is true. If True, then it will skip this little bit
#if false, then we run this code. We print "sorry no file exists", gets a new mouse button
#and a little nested while loop to check if the mouse button was on point, then we loop back
#to the while loop. Will loop through until True
while testFile == False:
    incorrectText = Text(Point(400,300), "Sorry, no file exists. Try again.")
    incorrectText.draw(win)
    mouse = win.getMouse()
    while mouse.getX()>500 and mouse.getX()<300 and mouse.getY()<500 and mouse.getY()>575:
        mouse = win.getMouse()
    entry = enter.getText()
    testFile = os.path.exists(entry+".txt")
    incorrectText.undraw()
    time.sleep(.5)

#for some otherworldly reason enter isn't undrawing
#so i have to do this instead
#it was glitching and just reapearing the instand it undrawed
#i tried absolutely everything and I think its a problem with graphics.py and tkinter
#because everything else undraws just fine, but this is the one thing that doesnt
#you can comment this out bellow to see what I mean
#I think it has to do with the fact that it's an entry box, and it can change
#so it can't undraw
#even if I move where the actual undraw text is in my code the same thing happens
#enter.move(800,800)
button.undraw()
word.undraw()
enter.undraw()
time.sleep(1)

#takes the input and turns it into text

inputFile = open(entry+".txt", "r")
read = inputFile.read()

#removes the words

#getting rid of useless clutter in the input string
read = read.replace(",","") 
read = read.replace("?","")
read = read.replace(".","")
read = read.replace("(","")
read = read.replace(")","")
read = read.replace(",","")
#keeping ' because it's used in words like I'll

lst = read.split() #split it by the spaces, gets it into a list
freq = {} #creating our dictionary
for words in lst:
    words = words.lower() #gets rid of case sensitive (there was overlap)
    if not (words in freq): #if we don't have the word yet
        freq[words] = 1 #create new entry with 1
    else:
        freq[words] = freq[words] + 1


#little stuff to get rid of stop words before I create wordList
file = open("stop_words.txt", "r")
reed = file.read()
#split into list of each word
#(one word per line in txt file)
stopWords = reed.splitlines()
#list of words that need to be removed
nullWords = []
for i in freq:
    for j in stopWords:
        if i == j:
            #can't immediately pop here, because dictionary
            #changes throughout, so it doesn't work
            #freq.pop(i)
            nullWords.append(i)
            
#for some reason, there were sometimes duplicates in nullWords
#gets rid of duplicates
nullWords2 = []
for i in nullWords:
    if i not in nullWords2:
        nullWords2.append(i)
        
#get rid of null words        
for word in nullWords2:
    freq.pop(word)
            
   

wordList = list(freq.items()) #now a list of tuples




#a full list of the coordinates so I can make them not overlap
coords = [] 
def main():
    for i in wordList:
        array = [] #creates new list every time we get a new tuple
        for j in i:
            array.append(j) #appends the 2 numbers of the array

        #setting the font size
        #was originally doing 10 * the number in the array, but 1 was too small and 10 was too big
        if array[1] == 1:
            fontSize = 13
        elif array[1] == 2:
            fontSize = 17
        elif array[1] <= 5:
            fontSize = int(array[1]) * 6
        elif array[1] <= 10:
            fontSize = int(array[1]) * 5
        elif array[1] > 10:
            fontSize = 57

        
#I spent way too long on this one while loop. I'll try my best to explain the whole thing
#initially set j equal to 5, so it can run through the for loop (and isn't 3 (i'll
#explain the significance later)) so 5, for loop starts. We get a random coordinate set,
#then we create a for loop for all of the coordinates that we have so far (they're in an array)
#then we check if overlap, and if it overlaps ONCE with any set of coords, we set j equal to 3,
#AND break. Break will end the for loop, so we don't redefine j, or get new coords and continue
#because j = 3, the if statement below isn't true, so therefore, it will run back through
#and create new coords to test again starting with the FIRST SET OF COORDS in the list
#however, if it can go through the entire coords list without setting off the boundary,
#then it sets j equal to 5, which SATISFIES the j!=3, which will set j equal to 1 which will
#end the while loop. I do know that you can easily simplify this, but it's working right now,
#and I don't want to touch it in case it breaks because then I will be really sad
        j=5
        while j>2:
            #setting x and y points to random ranges
            xPoint = random.randrange(50,750)
            yPoint = random.randrange(50,750)
            for i in coords:
                if (overlap(i[0], i[1], xPoint, yPoint)):
                    j=3
                    break
                else:
                    j=5
                    continue
            if j != 3:
               j = 1 

        #get the points in a tuple to put into the array of coordinates
        #appends AFTER it gets the final coords of the thing
        coords.append((xPoint,yPoint))
        #have to turn the string of array[0] into an actual string
        string = str(array[0])
        #creates the text with array[0] being the string, and at xPoint, yPoint
        text = Text(Point(xPoint, yPoint), string)
        #set the size to the predetermined size
        text.setSize(fontSize)
        #make it fancy
        text.setFace("courier")

        spin = random.randrange(1,3)
        #if spin == 1:
            #text.spin(90)
            
        text.draw(win)
        
    #closing    
    end = Text(Point(400,15), "Click anywhere to close")
    end.setFill("red")
    end.draw(win)
    win.getMouse()
    win.close()

    
#helps check if things overlap
def overlap(x,y,xVal,yVal):
    #can change these numbers if i want the words to be further apart, however,
    #if they're too big then the thing will break
    #smaller limits can fit more total words in them with slightly more overlap
    if (xVal >= x-100) and (xVal <= x+100) and (yVal >= y-50) and (yVal <= y+50):
        return True
    return False




main()

