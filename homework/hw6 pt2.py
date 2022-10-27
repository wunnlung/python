from graphics import *
import math
import time

def main():
    win = GraphWin("Kanye West!", 625,625)#creates a window
    square = Rectangle(Point(200,200), Point(425,425))#This is the square that we will operate on                      
    #win.setCoords(0,0, 625,625)                    #We haven't drawn it yet (we do it after we set the color)
    
#different color options
    #Green
    button1=Rectangle(Point(25,25), Point(100,100)) #These options will create a bunch of different buttons
    button1.setFill("green")
    button1.draw(win)
    button1Label = Text(Point(62,62),"green")
    button1Label.setFill("white")
    button1Label.draw(win)
    #Blue
    button2=Rectangle(Point(125,25), Point(200,100))
    button2.setFill("blue2")
    button2.draw(win)
    button2Label = Text(Point(162,62),"blue")
    button2Label.setFill("white")
    button2Label.draw(win)
    #Yellow
    button3=Rectangle(Point(225,25), Point(300,100))
    button3.setFill("yellow")
    button3.draw(win)
    button3Label = Text(Point(262,62),"yellow")
    button3Label.setFill("grey")
    button3Label.draw(win)
    #White
    button1=Rectangle(Point(325,25), Point(400,100))
    button1.setFill("white")
    button1.draw(win)
    button1Label = Text(Point(362,62),"white")
    button1Label.setFill("black")
    button1Label.draw(win)
    #Black
    button1=Rectangle(Point(425,25), Point(500,100))
    button1.setFill("black")
    button1.draw(win)
    button1Label = Text(Point(462,62),"black")
    button1Label.setFill("white")
    button1Label.draw(win)
    #Orange
    button1=Rectangle(Point(525,25), Point(600,100))
    button1.setFill("orange")
    button1.draw(win)
    button1Label = Text(Point(562,62),"orange")
    button1Label.setFill("white")
    button1Label.draw(win)

#ifs for the color
    pt=win.getMouse() #gets mouse click

    if pt.getX() >= 25 and pt.getX() <= 100 and pt.getY() >= 25 and pt.getY() <= 100: #Checks where the user clicks
        square.setFill("green")                                                     #sets the color based on what they select
    elif pt.getX()>=125 and pt.getX()<=200 and pt.getY()>=25 and pt.getY()<=100:
        square.setFill("blue2")
    elif pt.getX()>=225 and pt.getX()<=300 and pt.getY()>=25 and pt.getY()<=100:
        square.setFill("yellow")
    elif pt.getX()>=325 and pt.getX()<=400 and pt.getY()>=25 and pt.getY()<=100:
        square.setFill("white")
    elif pt.getX()>=425 and pt.getX()<=500 and pt.getY()>=25 and pt.getY()<=100:
        square.setFill("black")
    elif pt.getX()>=525 and pt.getX()<=600 and pt.getY()>=25 and pt.getY()<=100:
        square.setFill("orange")

    square.draw(win) #draws the square with the selected color
    for i in range(350):#moves out, then moves back in
        square.move(1,0)
    for i in range(350):
        square.move(-1,0)

#closing the window
    text = Text(Point(312,400), "Click anywhere to close")
    text.draw(win)
    win.getMouse()
    win.close()
    
    

main()
