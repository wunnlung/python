import random
from graphics import *

class MSDie:
    def __init__(self,numSides):
        self.sides = numSides
        self.value = 1
    def roll(self):
        self.value = random.randrange(1,self.sides+1)
        return self.value
    def getValue(self):
        return self.value
    def setValue(self,value):
        self.value=value


#die1 = MSDie(6)
#print(die1.roll())

def main():
    myDie = MSDie(6)
    yourDie = MSDie(10)
    print(myDie.sides)
    print(myDie.roll())
    print(myDie.getValue())

main()


#a class that creates a button object
class Button:
    def __init__(self, win, center, width, height, label):
        #creates a rectangular button
        x,y = center.getX(), center.getY()
        #edges of the button
        self.xmin = x-width/2
        self.xmax = x+width/2
        self.ymin = y-width/2
        self.ymax = y+width/2
        pt1 = Point(self.xmin,self.ymin)
        pt2 = Point(self.xmax,self.ymax)
        self.rect = Rectangle(pt1, pt2)
        self.rect.draw(win)
        self.words = Text(center, label)
        self.words.draw(win)





#def main():
 #   gwin = GraphWin("Button Test", 200, 200)
  #  x = Button(gwin, Point(100,100), 20, 30, "button")





