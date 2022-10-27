from graphics import *
from random import *

def main():
    win = GraphWin("I play fortnite", 800,800)
    win.setBackground("white")
    for x in range(250,350,2):
       # c1 = randrange(0,255)
        #c2 = randrange(0,255)
       # c3 = randrange(0,255)

        
        for y in range(200,300,2):
            p1 = Point(x,y)
            
            c1 = randrange(0,255)
            c2 = randrange(0,255)
            c3 = randrange(0,255)
            p1.setFill(color_rgb(c1,c2,c3))

            p1.draw(win)


    win.getMouse()
    win.close()
main()
