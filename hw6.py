#Todd Shriber
#hw6

from graphics import *

def main():
    win = GraphWin("I play fortnite", 800,800)
    for x in range(100,300,2): #for each x value (from left to right)
        for y in range(100,300,2): #create a whole column of Points (from up to down)
            p = Point(x,y)
            p.setFill("red")
            p.draw(win)

main()
#1: for the 2 in the for loop, the reason it works is because each point it draws is
#two pixels, instead of one.
#what this does is every time it draws a pixel, it will skip one, because it draws
#on that skipped pixel.

#2
# x       y
#100     100
#100     102
#100     104
#100     ...
#102     100
#102     102
#102     104
#102     ...
#300     300
