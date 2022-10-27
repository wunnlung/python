from graphics import *
import math
import time
from button import *

def main():
    win = GraphWin("When the impostor is SUS", 800,800)
    inputBox = Entry(Point(400,400), 50)
    inputBox.draw(win)
    drawButton(win, Point(100,100), Point(200,150), "Lower Case!")
    drawButton(win, Point(300,100), Point(400,150), "Smush!")
    drawButton(win, Point(500,100), Point(600,150), "Reverse!")
    drawButton(win, Point(700,100), Point(800,150), "Palindrome?")

    exitButton = drawButton(win, Point(800,800), Point(700,700), "exit")
    
    pt = win.getMouse()
    while not(pt.getX()<=800 and pt.getX()>=700 and pt.getY()<=800 and pt.getY()>=700):
        if pt.getX()<=200 and pt.getX()>=100 and pt.getY()<=150 and pt.getY()>=100:
            x = inputBox.getText()
            userString = x.lower()
            text = Text(Point(400,600), userString)
            text.draw(win)
            pt = win.getMouse()
        elif pt.getX()<=400 and pt.getX()>=300 and pt.getY()<=150 and pt.getY()>=100:
            x = inputBox.getText()
            string = smush(x)
            text = Text(Point(400,600), string)
            text.draw(win)
            pt = win.getMouse()
        elif pt.getX()<=600 and pt.getX()>=500 and pt.getY()<=150 and pt.getY()>=100:
            x = inputBox.getText()
            string = reverse(x)
            text = Text(Point(400,600), string)
            text.draw(win)
            pt = win.getMouse()
        elif pt.getX()<=800 and pt.getX()>=700 and pt.getY()<=150 and pt.getY()>=100:
            x = inputBox.getText()
            if isPalindrome(x) == True:
                text = Text(Point(400,600), "Yes! its a palindrome!")
                text.draw(win)
            else:
                text = Text(Point(400,600), "No Sorry! Not a palindrome")
                text.draw(win)
            pt = win.getMouse()
        text.undraw()
    win.close()
        

    
def smush(originalStr):
    y = originalStr.replace(" ", "")
    return y

def reverse(originalStr):
    z = originalStr[::-1]
    return z

def isPalindrome(phrase):
    x = phrase[::-1]
    y = x.lower()
    reverse = y.replace(" ", "")
    if phrase == reverse:
        return True
    else:
        return False

main()
    

