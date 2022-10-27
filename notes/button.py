#COM 110 Graphical User Interfaces (GUIs)
#button.py program
#
#This program creates a GUI with two buttons.
#Depending which button the user clicks, a circle or square is drawn.
#
#(If you finish this exercise early, practice and explore:
#  think about ways you can make the code more modular/organized.
#  You might also consider adding functionality to the program,
#  like a way for the user to specify what color the object is drawn, etc.)
#

from graphics import *
import math
import time

def main2():
    
    win=GraphWin("Button GUI", 800,800)

    #Set the coordinates in the window so that
    #the lower left corner is the point (0, 0)
    #and the upper right corner is the point (100, 100).
    #This way the values along the y-axis increase
    #going upward, like in math class.
    win.setCoords( 0,0, 100,100)
    #Note that given the dimensions of the graphical window,
    #(defined above as 800x800)
    #this means that the x-axis now has 8 pixels between "tick marks"
    #and the y-axis also 8 pixels between "tick marks"

    #Now, create "button" 25 ticks over and 90 ticks up
    button1=Rectangle(Point(25,96), Point(35,90))
    button1.setFill("blue3")
    button1.draw(win)
    #Put label on button
    button1Label = Text(Point(30,93),"Circle")
    button1Label.setFill("white")
    button1Label.draw(win)

    #Adding a second button here that says Square
    button2=Rectangle(Point(65,96), Point(75,90))
    button2.setFill("blue3")
    button2.draw(win)
    #Put label on button
    button2Label = Text(Point(70,93),"Square")
    button2Label.setFill("white")
    button2Label.draw(win)

    exitButton = drawButton(win, Point(100, 100), Point(90,90), "Exit")
    

    
    pt=win.getMouse()


    while not(pt.getX() >= 90 and pt.getX() <= 100 and pt.getY()>=90 and pt.getY()<=100): 
        if pt.getX()>=25 and pt.getX()<=35 and pt.getY()>=90 and pt.getY()<=96: 
        
            shape=Circle(Point(50,50),20)
            shape.setFill('red')
            shape.draw(win)
            pt=win.getMouse()
            shape.undraw()
    
        elif pt.getX() >= 65 and pt.getX() <= 75 and pt.getY()>=90 and pt.getY()<=96:
            shape = Rectangle(Point(25,25), Point(75,75))
            shape.setFill("blue")
            shape.draw(win)
            pt=win.getMouse()
            shape.undraw()
        else:
            pt=win.getMouse()
            
    

    
    win.close()


#main()

def distance(x1,y1,x2,y2):
    deltax = x2-x1
    deltay = y2-y1
    c = deltax**2 + deltay**2
    dist = math.sqrt(c)
    return dist

def drawCircle(gwin, radius, locx, locy, color):
    circ = Circle(Point(locx,locy), radius)
    circ.setFill(color)
    circ.draw(gwin)


def drawButton(gwin,pt1,pt2,label):
    button = Rectangle(pt1,pt2)
    button.setFill("blue3")
    button.draw(gwin)
    midPoint = Point((pt1.getX() + pt2.getX())/2, (pt1.getY() + pt2.getY())/2)
    buttonLabel1 = Text(midPoint, label)
    buttonLabel1.setFill("white")
    buttonLabel1.draw(gwin)

def main():
    win=GraphWin("Button GUI", 800,800)
    HEIGHT = 100
    WIDTH = 100
    win.setCoords(0,0, HEIGHT, WIDTH)

    drawButton(win, Point(25,96), Point(35,90), "Circle")
    drawButton(win, Point(65,96), Point(75,90), "Square")
    drawCircle(win, 15, 50, 50, "blue")
    

password = "ABCD1234"
i = input("enter password here: ")
while i != password:
    i = input("That was incorrect. Try again: ")
main2()


