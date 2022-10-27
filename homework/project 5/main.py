#for all info check README.txt

from graphics import *
from turtle import *
from class_button import *
from solver import *
from fractal import *
import math


#created a new dictionary to use because the other one was inconsistent with upper case and lower case letters
#h = open("words2.txt", "w")
#inputIle = open("words.txt", "r")
#r = inputIle.read()
#s = r.splitlines()
#for i in s:
 #   h.write(i.lower())
  #  h.write("\n")


def main2():
    #just a side note, right now it takes a while to undraw everything when user restarts
    #if the win was set inside of the while loop, it would get rid of that time, but
    #just reset the window every time the user wanted to loop in
    #basic graphic stuff
    win = GraphWin("hehe", 800,800)
    win.setBackground("white")

    #start the loop    
    restart = True
    while restart == True:
        #basic graphic stuff if you want undrawing faster
        #win = GraphWin("hehe", 800,800)
        #win.setBackground("white")
        
        #decide which function to do
        start_choice = Text(Point(400,400), "Please Select Which function you would like to do")
        start_choice.draw(win)
        fractal = Button(win, Point(200, 600), 150, 100, "Fractal Drawing")
        solver = Button(win, Point(600, 600), 150, 100, "Word Jumble Solver")

        #goes until user clicks a button
        pt = win.getMouse()
        while not (fractal.clicked(pt) or solver.clicked(pt)):
            pt = win.getMouse()

        #undraws
        start_choice.undraw()
        fractal.undraw()
        solver.undraw()

        #do this if the user clicked on the fractal option
        if fractal.clicked(pt):
            #labels and entry objects
            c_label = Text(Point(200, 130), "Pick A curve: Enter \"tree\" or \"c\"")
            c_label.draw(win)
            Curve = Entry(Point(200,150), 50)
            Curve.draw(win)
            l_label = Text(Point(200, 230), "Enter in an Integer for the Length (100 for tree and 400 for c works best)")
            l_label.draw(win)
            Length = Entry(Point(200, 250), 50)
            Length.draw(win)
            ll_label = Text(Point(200, 330), "Enter in an Integer for the Level (no greater than 10)")
            ll_label.draw(win)
            Level = Entry(Point(200, 350), 50)
            Level.draw(win)
            start = Button(win, Point(400,500), 75, 50, "Start")
            qb = Button(win, Point(750,750), 50, 50,"Quit")

            #check if user clicks start button
            pt = win.getMouse()
            while not start.clicked(pt):
                if qb.clicked(pt):
                    restart = False
                    win.close()
                    #just end the function
                    return
                pt = win.getMouse()

            #getting the text from the entry objects
            cur = Curve.getText()
            l = int(Length.getText())
            l2 = int(Level.getText())

            #undrawing
            c_label.undraw()
            Curve.undraw()
            l_label.undraw()
            Length.undraw()
            ll_label.undraw()
            Level.undraw()
            start.undraw()
            
            t = Turtle(win)

            if cur.lower() == "tree":
                t.moveTo(Point(200,400))
                tree(t, l, l2)
            elif cur.lower() == "c":
                t.moveTo(Point(200,500))
                c(t, l, l2)

            #to restart the code or not
            end = Button(win, Point(400, 125), 100, 75, "Restart?")
            pt = win.getMouse()
            while not end.clicked(pt):
                if end.clicked(pt):
                    restart = False
                    win.close
                    return
                pt = win.getMouse()

            #clear window to reset
            clear(win)

        #if user originally clicked on word jumble solver
        else:
            welcome=Text(Point(400,150),"Enter a word")
            welcome2=Text(Point(400,250),"python will run through all combinations of the letters and give you all formed words")
            welcome.setSize(24)
            welcome2.setSize(12)
            welcome.draw(win)
            welcome2.draw(win)
            user_input = Entry(Point(400,400), 50)
            user_input.draw(win)
            warning=Text(Point(400,700),"Do not enter words longer then 6 characters as it might crash")
            warning.setSize(14)
            warning.draw(win)
            button = Button(win, Point(400,500), 200,50, "start")
            qb = Button(win, Point(750,750), 50, 50,"Quit")
            OutWords = Text(Point(400, 550), "Output Words")
            OutWords.setSize(25)
            p = win.getMouse()
            while not button.clicked(p):
                if qb.clicked(p):
                    resart = False
                    win.close()
                    return
                p = win.getMouse()
            inputFile = open("words2.txt", "r")
            read = inputFile.read()
            dictionary = read.splitlines()
            words = []
            temp = perm(words, user_input.getText())
            #print(temp)
            final = []
            for i in temp:
                for j in dictionary:
                    if i == j:
                        final.append(i)
                        #break
            fin = []

            for i in final:
                if i not in fin:
                    fin.append(i)

            #print(fin)
            OutWords.draw(win)
            x=len(fin)
            #checks if the word actually has any outputs
            if x != 0:
                OW= Text(Point(400,600),fin)
                if x > 7:
                    OW.setSize(16)
                if x<7 and x>5:
                    OW.setSize(18)
                if x<5 and x>3:
                    OW.setSize(22)
                if x<3:
                    OW.setSize(28)
            else:
                OW= Text(Point(400,600),"No words were found")
                
            OW.draw(win)
            
            #to restart the code or not
            end = Button(win, Point(400, 75), 100, 75, "Restart?")
            pt = win.getMouse()
            while not end.clicked(pt):
                if qb.clicked(pt):
                    restart = False
                    win.close()
                    return
                pt = win.getMouse()

            #clear window to reset
            clear(win)

              



#method to remove all objects from the window
def clear(win):
    #for all items in the window
    for item in win.items[:]:
        #undraw everything
        item.undraw()
    #then update the window
    win.update()
            

main2()



