from graphics import *
import random
import time

def main():
    
    win = GraphWin("Fun #5", 600, 600)

    square = Rectangle(Point(200,200),Point(400,400))
    square.draw(win)
    
    pt = win.getMouse()
    while pt.getX()<=400 and pt.getX()>=200 and pt.getY()<=400 and pt.getY()>=200:
        a=random.randrange(0,255)
        b=random.randrange(0,255)
        c=random.randrange(0,255)
        square.setFill(color_rgb(a,b,c))
        pt=win.getMouse()
    win.close()


   # win.getMouse()
    #win.close()

#main()

def average():
    x = int(input("enter a number here: "))
    array = []
    while x>=0:
        array.append(x)
        x = int(input("enter another number here: "))
    print(sum(array)/len(array))


#average()

def password():
    PASSWORD = "Camels" 
    userpass = input("Enter the password to use this program: ")
    while userpass != PASSWORD: 
        userpass = input("Sorry wrong password.  Try again --> ")

password()





    
