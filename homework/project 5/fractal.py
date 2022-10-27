from graphics import *
from turtle import *
from class_button import *
import math

def tree(turtle, length, level):
    #if the length is less than length / recusrion level:
    #if length < (length/level):
    if level == 0:
        #end the function  
        return
    #draw the branch
    turtle.draw(length)
    #turn left 45 degrees
    turtle.turn(-pi/4)
    #create a new branch .75x the length of the last branch
    tree(turtle, length*0.75, level - 1)
    #turn right for next branch
    turtle.turn(pi/2)
    #creates the second branch
    tree(turtle, length*0.75, level - 1)
    #rotates back to the original angle
    turtle.turn(-pi/4)
    #move back to the original position
    turtle.draw(-length)       
    return              


def c(turtle, length, level):
    if level == 0:
        turtle.draw(length)
    else:
        #turn left 45 degrees
        turtle.turn(-pi/4)
        #draw a c-curve of size length/sqrt(2)
        c(turtle, length/math.sqrt(2), level - 1)
        #turn right 90 degrees
        turtle.turn(pi/2)
        #draw a c-curve of size length/sqrt(2)
        c(turtle, length/math.sqrt(2), level - 1)
        #turn left 45 degrees
        turtle.turn(-pi/4)
        
