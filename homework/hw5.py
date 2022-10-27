from graphics import *
from time import *

 
def main():
    win=GraphWin("Fun!", 400,600)

    square=Rectangle(Point(100,100),Point(300,300))
    square.setFill("blue")
    square.draw(win)
    text = Text(Point(200,200),"This is a blue Square\nClick to see it move") #this will create a text box at 200,200
    text.draw(win) #this will print said text box inside the window (draw(win))
    win.getMouse() #pauses and waits for user click to continue
    text.undraw() #sadly can't just edit the text halfway through, so I need to erase it and make a new text
    text2 = Text(Point(200,200),"This is a FLASHING Sqaure!\nits moving now!!") #recreating text, at same spot, so this one can move
    text2.draw(win) #putting it in the code
    for i in range(310):
        square.move(1,0)
        square.setFill("blue") #for every time it loops around to move, it will change color, then reset it, then change it again
        text2.move(1,0)      #same line as above pretty much, so it moves at the same speed and to the same location
        #sleep(0.02)     #pause .02 seconds at the end of each iteration
        square.setFill("red") #changes the color
    for i in range(310):
        square.move(-1,0)
        square.setFill("blue") #I wasn't exactly sure what it meant by moving partway through, so I'm just gonna do it this way
        text2.move(-1,0)
        square.setFill("pink")

    sendoff = Text(Point(200,400),"Click anywhere to close.")
    sendoff.draw(win)
    win.getMouse()
    win.close()


main()

#its a lot to explain up there, so I'll do it down here.
#pretty much how the move works, is it will move by a specific amount, which is specified by the dx,dy
#dx being the x axis and dy being the y axis
#but, it only moves it a single time. But if we put it in a for loop, we can make it look like its moving smoothly, instead of just teleporting,
#because we move it 310 times to the right by one pixel

