from graphics import *
from time import *

 
def main():
    x = input("what color would you like to select?: ")
    teext = "This is a", x, "Square\nClick to see it move"
    win=GraphWin("Kanye West!", 400,600)

    square=Rectangle(Point(100,100),Point(300,300))
    square.setFill(x)
    square.draw(win)

    text = Text(Point(200,200),teext) #this will create a text box at 200,200
    text.draw(win) #this will print said text box inside the window (draw(win))
    win.getMouse() #pauses and waits for user click to continue
    for i in range(310):
        square.move(1,0)
        text.move(1,0)         

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

