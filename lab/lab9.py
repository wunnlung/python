from class_button import *
from graphics import *
from dieview import *
import random

def main():
    win = GraphWin("fortnite balls", 500,500)
    win.setBackground("green")
    rollButton = Button(win, Point(250,300), 75,35, "Roll")
    quitButton = Button(win, Point(250,400), 50,25, "Quit")
    rollButton.activate()
    die1 = DieView(win, Point(150,100), 75)
    die2 = DieView(win, Point(350,100), 75)
    p = win.getMouse()
    quitButton.activate()
    while quitButton.isClicked(p) == False:
        if rollButton.isClicked(p) == True:
            roll1 = random.randrange(1,7)
            roll2 = random.randrange(1,7)
            die1.setValue(roll1)
            die2.setValue(roll2)
        elif p.getX()<=225 and p.getX()>=75 and p.getY()<=175 and p.getY()>=25:
            roll1 = random.randrange(1,7)
            die1.setValue(roll1)
        elif p.getX()<=425 and p.getX()>=275 and p.getY()<=175 and p.getY()>=25:
            roll2 = random.randrange(1,7)
            die2.setValue(roll2)
        else:
            print("hehe")
        p = win.getMouse()
    win.close()

    
    
    
main()
