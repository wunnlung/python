#Button Class

from graphics import *

class Button:
    def __init__(self, win, center, width, height, label):
        x, y = center.getX(), center.getY()
        self.xmin = x - width/2
        self.xmax = x + width/2
        self.ymin = y - height/2
        self.ymax = y + height/2
        pt1 = Point(self.xmin, self.ymin)
        pt2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(pt1,pt2)
        self.rect.draw(win)
        self.words = Text(center, label)
        self.words.draw(win)
    
        
    def deactivate(self):
        """sets this button to deactivated, not clickable"""
        #set text color gray, set outline to be thinner
        self.words.setTextColor("dark grey")
        self.rect.setWidth(1)
        self.activate = False
        #set boolean flag to False



    def activate(self):
        """sets this button to activated"""
        #set text back to black, set bolder outline
        self.words.setTextColor("black")
        self.rect.setWidth(2)
        self.activate = True
        #set bootlean flag to True

    def isClicked(self, pt):
        #if click inside, return true
        if self.activate and \
           (self.xmin <= pt.getX() <= self.xmax) and \
           (self.ymin <= pt.getY() <= self.ymax):
            return True
        else:
            #else, return false
            return False
        #this is the mosst important line
        print("willem suks at koding and bad")
           
        """returns True if pt is within the boundaries of Button"""
        
        


##def test():
##    gwin = GraphWin("Button Test", 200,200)
##    myButton = Button(gwin, Point(100,100), 50, 25, "Quit")
##    p = gwin.getMouse()
##    myButton.activate()
##    if myButton.isClicked(p):
##        print("Button clicked")
##    else:
##        print("Button not clicked")
##test()
