#Todd Shriber, Project 3
#
#what this code does it it creates a gui that the user can code
#and decode messages. They input their line of text, and a key.
#with that, the code runs and spits out the coded or decoded message.
#then the user has the option to code/decode another message,
#or terminate the program
#this program also has the option to guess what a coded word is
#and return the key and the word itself
#
#just as a little suggestion, when testing the guess function,
#i used "nkrru" which returns "hello" with a key of 6
#i did test out a bunch of other things, but here is one in case you need it :)
#also for inputFile, I have a sample one if you want to use, called biden.txt
#yes, I did take it directly from lab 3



from graphics import *
from button import *
import time
import math


#give the user the option to input a text file, or to not input a text file
#this will come up at the very end of the code, when I either call main() or main2()
question = int(input("what would you like to do?\n1. Input text file\n2. User input\n3. Computer guess\n"))


#setting all the graphics for the window
win = GraphWin("Caesar encoder", 800,800)
win.setBackground("white")

#a little thing I felt added to the ambience
vines = Image(Point(400,325), "vines.png")
#originally had this title, but I'm gonna animate it
#title = Text(Point(400, 200), "Caesar Encoder!")
#title.setSize(18)

#have each letter in it's own thing
C = Text(Point(300, 200), "C")
a = Text(Point(310, 200), "a")
e = Text(Point(320, 200), "e")
s = Text(Point(330, 200), "s")
a2 = Text(Point(340, 200), "a")
r = Text(Point(350, 200), "r")
space = Text(Point(360, 200), " ")
E2 = Text(Point(370, 200), "E")
n = Text(Point(380, 200), "n")
c2 = Text(Point(390, 200), "c")
o = Text(Point(400, 200), "o")
d = Text(Point(410, 200), "d")
e3 = Text(Point(420, 200), "e")
r2 = Text(Point(430, 200), "r")

#draw each letter
C.draw(win)
time.sleep(.3)
a.draw(win)
time.sleep(.3)
e.draw(win)
time.sleep(.3)
s.draw(win)
time.sleep(.3)
a2.draw(win)
time.sleep(.3)
r.draw(win)
time.sleep(.3)
space.draw(win)
time.sleep(.3)
E2.draw(win)
time.sleep(.3)
n.draw(win)
time.sleep(.3)
c2.draw(win)
time.sleep(.3)
o.draw(win)
time.sleep(.3)
d.draw(win)
time.sleep(.3)
e3.draw(win)
time.sleep(.3)
r2.draw(win)


#some pillars
pillar1 = Image(Point(200,400), "pillar.png")
pillar2 = Image(Point(600, 400), "pillar2.png")

#changing the font for the title
#title.setFace("courier")
#title.draw(win)
vines.draw(win)
pillar1.draw(win)
pillar2.draw(win)

#draws 2 buttons
#added my own code to the drawButton
#now I can also set the font
code = drawButton(win, Point(150,550), Point(300, 650), "Code", "courier")
decode = drawButton(win, Point(500,550), Point(650, 650), "Decode", "courier")
#little wreaths for the buttons
wreath1 = Image(Point(225,615), "wreath.png") #just a little photo
wreath2 = Image(Point(575, 615), "wreath2.png")
wreath1.draw(win) 
wreath2.draw(win)

#originally had text1 here, but moved it so it can change
#so if main() is run, it will say "input text"
#and if main2() is run, it will say "input name of file"
#also had inputKey here, but moved it since I dont want it for the bonus

#only draws
if question == 1 or question == 2:
    text2 = Text(Point(600, 230), "Input Key:")
    text2.setFace("courier") #changes font
    text2.draw(win)
    inputKey = Entry(Point(600,255), 5)
    inputKey.draw(win)

inputText = Entry(Point(200, 255), 25) #one box for input
inputText.draw(win)


#main functions
##########################################################################################
##########################################################################################


#changing input boxes doesnt count as a mouse click
def main():
    text1 = Text(Point(130,230), "Input Text:")
    text1.setFace("courier") #changes font
    text1.draw(win)
    
    i = 7
    #have a while loop, so it can continue to code and decode if the user wants it to. Else, it ends the program
    while i > 6:
        pt = win.getMouse()
        t = inputText.getText()
        k = inputKey.getText()
        output = Rectangle(Point(300,700), Point(500, 725))
        output.setFill("grey")
        output.draw(win)
        if pt.getX()<=300 and pt.getX()>=150 and pt.getY()<=650 and pt.getY()>=550:
            #runs t,k through code func
            #sets it as the stirng, "string"
            string = code(t,k)
            #create text box with string from code func
            final = Text(Point(400,710), string)
            final.draw(win)
        elif pt.getX()<=650 and pt.getX()>=500 and pt.getY()<=650 and pt.getY()>=550:
            string = decode(t,k)
            final = Text(Point(400,710), string)
            final.draw(win)
        #after the click, generates a button to "continue the program"
        #originally tried to use drawButton, but I am unable to undraw the button
        endBox = Rectangle(Point(330,425), Point(470,500))
        endBox.setFill("green")
        endMessage = Text(Point(400,460), "Do you want to\n code something else?\nclick here for yes!\nClick\
 anywhere else for no")
        endBox.draw(win)
        endMessage.draw(win)
        pt2 = win.getMouse()
        #if click button, continue, else, end
        if pt2.getX()<=460 and pt2.getX()>=340 and pt2.getY()<=500 and pt2.getY()>=425:
            i=7
            #continues and undraws everything
            output.undraw()
            final.undraw()
            endMessage.undraw()
            endBox.undraw()
        else:
            #sets i to 5, which is less than 6
            #ends the while loop
            i = 5
            win.close()



def main2():
    text1 = Text(Point(150,230), "Input File Name (with .txt):")
    text1.setFace("courier") #changes font
    text1.draw(win)
    
    pt = win.getMouse() #gets mouse button
    text = inputText.getText() 
    k = inputKey.getText()
    #opens a file with the name that was inputted
    inputFile = open(text, "r")
    #turns that file into a string
    bookString = inputFile.read()
    #and then IT JUST RUNS IT RIGHT ON THROUGH THE CODE I ALREADY WROTE
    if pt.getX()<=300 and pt.getX()>=150 and pt.getY()<=650 and pt.getY()>=550:
        output = code(bookString, k)
        #writes an output text file
        outputFile = open("outputFile.txt", "w")
        outputFile.write(output)
        outputFile.close()
    elif pt.getX()<=650 and pt.getX()>=500 and pt.getY()<=650 and pt.getY()>=550:
        output = decode(bookString, k)
        outputFile = open("outputFile.txt", "w")
        outputFile.write(output)
        outputFile.close()
    endBox = Rectangle(Point(330,425), Point(470,500))
    endBox.setFill("green")
    endMessage = Text(Point(400,460), "Check the folder\nfor your created file!\nClick anywhere to close")
    endBox.draw(win)
    endMessage.draw(win)
    win.getMouse()
    win.close()
    #I could have it loop back with a while loop, but that would mess with the output file it creates
    #Because it creates a file with the same name, it will just rewrite the same file
    #so it will just ruin the original thing



#The for loops are a little confusing so I will try my best to explain them here
#first its the original while loop, that keeps it running if k>8
#then the first if, which will see if the user clicked inside of the box
#if they didn't, then we can go all the way to the bottom here and see that
#it just will loop back until they do click there
#and then we have if key == None
#what this does is just in case Guess() doesn't return anything valid,
#it will say "hey sorry word not real haha"
#but that is matched below with an else, which will print the output (if valid)
#and then inside key == None and its matching else there are identical for loops,
#so I will only explain one of them (since theyre the exact same)
#the program will pop up a little thing that asks if the user wants to end the code
#if they click in the box, it loops back to the beginning and undraws everything
#if they click outside, then it will close the program and end the loop
#I'm Todd, and thank you for reading my Todd Talk #jokes


def mainBonus():
    butt = drawButton(win, Point(350,350), Point(450,450), "GUESS?", "courier")
    k=9
    while k>8: #loops until it gets the mouse click
        pt = win.getMouse()
        txt = inputText.getText()
        if pt.getX()<=450 and pt.getX()>=350 and pt.getY()<=450 and pt.getY()>=350:
            key = guess(txt)
            #in case it doesnt know the word
            if key == None:
                final = Text(Point(400,710), "Sorry, it doesn't seem your word is in our dictionary.")
                final.draw(win)
                #ending
                endBox = Rectangle(Point(330,425), Point(470,500))
                endBox.setFill("green")
                endMessage = Text(Point(400,460), "Do you want to\ninput something else?\nclick here for yes!\nClick\
 anywhere else for no")
                endBox.draw(win), endMessage.draw(win)
                pt2 = win.getMouse()
                if pt2.getX()<=460 and pt2.getX()>=340 and pt2.getY()<=500 and pt2.getY()>=425:
                    k=9
                    #continues and undraws everything
                    final.undraw()
                    endMessage.undraw()
                    endBox.undraw()
                else:
                    k=7
                    win.close()     

            #if there is a valid input
            else:
                word = decode(txt,key)
                message = f'your word is {word}, with a key of {key}'
                final = Text(Point(400,710), message)
                final.draw(win)
                #print(key)
                #ending
                endBox = Rectangle(Point(330,425), Point(470,500))
                endBox.setFill("green")
                endMessage = Text(Point(400,460), "Do you want to\ninput something else?\nclick here for yes!\nClick\
 anywhere else for no")
                endBox.draw(win), endMessage.draw(win)
                pt2 = win.getMouse()
                if pt2.getX()<=460 and pt2.getX()>=340 and pt2.getY()<=500 and pt2.getY()>=425:
                    k=9
                    #continues and undraws everything
                    final.undraw()
                    endMessage.undraw()
                    endBox.undraw()
                else:
                    k=7
                    win.close()     
        else:
            k=9 #continues the loop
            #goes until a valid mouse click
    
    


#helper functions
##########################################################################################
##########################################################################################





def code(text, key):
    message = ""
    for i in text:
        #if space or symbol, just add those to the message
        if i == " " or i == "." or i == "," or i == "!":
            message += i
        else:
            #J is the coded number, but it might not be correct...
            j = ord(i) + int(key)
            #Use below to check if the J number is always correct
            #checks if upper case
            if ord(i) >= 65 and ord(i) <= 90:
                #checks if letter + key creates a symbol
                if j >= 91:
                    #will have j loop back around, if > 91
                    j = (j - 91) + 65
                    #no else, because if else, we don't change j
            #now does same thing for lower case
            elif ord(i) >= 97 and ord(i) <= 122:
                if j >= 123:
                    j = (j - 123) + 97
                    
            letter = chr(j)
            message += letter
    #returns final message as string
    
    return message


#code is mostly the same as code(text,key)
#main difference is j is i MINUS key instead of plus
def decode(text, key):
    message = ""
    for i in text:
        if i == " " or i == "." or i == ",":
            message += i
        else:
            j = ord(i) - int(key)
            if ord(i) >= 65 and ord(i) <= 90:
                #checks if letter + key creates a symbol
                if j <= 64:
                    #sees how far away it is from 65
                    #subtracts that from 92 (the end)
                    j = (j-65) + 91
            #now does same thing for lower case
            elif ord(i) >= 97 and ord(i) <= 122:
                if j <= 96:
                    j = (j - 97) + 123
                    
            letter = chr(j)
            message += letter

            
    return message




def guess(text):
    #opens dictionary
    file = open("words.txt", "r")
    #my dictionary array
    dictionary = []
    for i in file:
        strip = i.strip()
        split = strip.split()
        #print(split)
        dictionary.append(split)    
#for some reason this turns it into a list of lists?
#not sure why it does that, its kinda weird of you to do that python
#but this (sadly found from google D:) will make it not a list of lists
#but instead a list of STRINGS
#it kept on not working for me and I was getting so frustrated at it
#but I FINALLY GOT IT
    flattened = []
    for sublist in dictionary:
        for val in sublist:
            flattened.append(val)

    #idk what the max key is supposed to be but here is every letter
    #in the alphabet
    for i in range(26):
        word = decode(text, i)
        for j in flattened:
            if word == j:
                return i
    #returns null if can't find word
    return None
        




#runs either main or main2, depending on user input
#main2 is input file, main is input text
if question == 1:
    main2()
elif question == 2:
    main()
elif question == 3:
    mainBonus()













