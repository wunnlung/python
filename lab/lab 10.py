from turtle import *
from graphics import *
import math

def main():
    win = GraphWin("hehe", 800,800)
    win.setBackground("white")
    t = Turtle(win)
##    t.moveTo(Point(350,400))
##    t.draw(100)
##    t.moveTo(Point(400,400))
##    t.turn(math.pi/2)
##    t.draw(150)
##    t.moveTo(Point(500,400))
##    t.turn(math.pi/2)
##    for i in range(35):
##        t.draw(5)
##        t.turn(-.1)
##    #t.turn(math.pi/2)
##    for i in range(35):
##        t.draw(5)
##        t.turn(.1)
    t.moveTo(Point(200,200))
##    f = 500
##    while f>0:
##        spiral(t, f)
##        f -= 25
    
    kcurve(t, 400, 5)
    t.turn(2*math.pi/3)
    kcurve(t, 400, 3)
    t.turn(2*math.pi/3)
    kcurve(t, 400, 1)
    

    

def spiral(turtle, i):
    turtle.draw(i)
    turtle.turn(math.pi/2)
    i += 25

main()
