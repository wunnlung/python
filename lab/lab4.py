from graphics import *
from random import *

def main():
    win=GraphWin("Kanye West", 800,800)
    c1 = 135
    c2 = 206
    c3 = 250
    win.setBackground(color_rgb(c1,c2,c3))
  #  point = Point(500,500)
   # point.setFill("red")
    #point.draw(win)

    #sun
    sun = Circle(Point(100, 100), 75)
    sun.setFill("yellow")
    sun.draw(win)

    #moon
    moon = Circle(Point(700,800), 75)
    moon.setFill("white")
    moon.draw(win)

    #lawn
    lawn = Rectangle(Point(0,650), Point(800,800))
    lawn.setFill("lime green")
    lawn.draw(win)

    #house
    base = Rectangle(Point(250,700), Point(550,375))
    base.setFill("brown4")
    base.draw(win)

    #roof
    triangle = Polygon(Point(400,200), Point(600,375), Point(200,375))
    triangle.setFill("rosybrown")
    triangle.draw(win)

   

    

    #move sun
    for i in range(350):
        if i >= 250:
            x = randrange(10,790)
            y = randrange(10,600)
            point = Point(x,y)
            point.setFill("white")
            point.draw(win)
            base = Rectangle(Point(250,700), Point(550,375))
            base.setFill("brown4")
            base.draw(win)
            triangle = Polygon(Point(400,200), Point(600,375), Point(200,375))
            triangle.setFill("rosybrown")
            triangle.draw(win)
        sun.move(0,2)
        moon.move(0,-2)
        if c1 > 0:
            c1 = c1 - 1
        if c2 > 0:
            c2 = c2 - 1
        if c3 > 0:
            c3 = c3 - 1
        win.setBackground(color_rgb(c1,c2,c3))

    #night sky
    win.setBackground("black")

    
    win.getMouse()
    win.close()

    
main()
