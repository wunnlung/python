from dieview import *


class colorDieView(DieView):
    def __init__(self, win, center, size):
        super().__init__(win, center, size)

    #i don't really need this as I have setValue from the super()
    #nvm setcolor doesnt run without this, as it doesnt have self.value
    def setValue(self, value):
        self.value = value
        DieView.setValue(self, value) 

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)

#ok I kinda have a lot to say about this little bit
#originally, i wrote this code without the setvalue func, as i thought I didn't
#need it. I thought i didnt because in the init for the class, I added super,
#which pretty much just inherits everything from the parent class; both the
#inits and the overall functions. Unfortunately, when I didn't have setValue,
#setcolor would give an error. It said that there was no self.value, which
#makes sense, as it wasn't defined. So I thought I would be all cool and just
#comment out that part. Then I took a look at the parent code. I noticed that
#there was a background and foreground in the initializer. However, it wouldn't
#get called until it needed pips to be made, which was everytime you set a
#value, and on the original instance. Very interesting! So because it would set
#the initial color to black, and then I didn't rerun the setValue from DieView,
#the pips would never reset, which wouldn't make it change color. 
def main():
    win = GraphWin("hehe", 800,800)
    die1 = colorDieView(win, Point(400,400), 100)
    win.getMouse()
    die1.setColor("green")
    #die1.setValue(3)
    #die1.setColor("green")
    win.getMouse()
    win.close()

main()
        
        
