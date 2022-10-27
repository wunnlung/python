from class_button import *

#gets all the possible word combinations
def perm(words, rem, fullWord=''):
    if len(rem) == 0:
        words.append(fullWord)
        #print(candidate)

    for i in range(len(rem)):
        newWord = fullWord + rem[i]
        newRem = rem[0:i] + rem[i + 1:]

        perm(words,newRem, newWord)
    return words

#lst = []
#print(perm(lst, "ABC"))

#run moved to main function

##def run(win):
##    welcome=Text(Point(400,150),"Enter a word")
##    welcome2=Text(Point(400,250),"python will run through all combinations of the letters and give you all formed words")
##    welcome.setSize(24)
##    welcome2.setSize(12)
##    welcome.draw(win)
##    welcome2.draw(win)
##    user_input = Entry(Point(400,400), 50)
##    user_input.draw(win)
##    warning=Text(Point(400,700),"Do not enter words longer then 6 characters as it might crash")
##    warning.setSize(14)
##    warning.draw(win)
##    button = Button(win, Point(400,500), 200,50, "start")
##    qb = Button(win, Point(750,750), 50, 50,"Quit")
##    OutWords = Text(Point(400, 550), "Output Words")
##    OutWords.setSize(25)
##    p = win.getMouse()
##    while not button.clicked(p):
##        if qb.clicked(p):
##            win.close()
##        p = win.getMouse()
##    inputFile = open("words.txt", "r")
##    read = inputFile.read()
##    dictionary = read.splitlines()
##    words = []
##    temp = perm(words, user_input.getText())
##    #print(temp)
##    final = []
##    for i in temp:
##        for j in dictionary:
##            if i == j:
##                final.append(i)
##                #break
##    fin = []
##
##    for i in final:
##        if i not in fin:
##            fin.append(i)
##
##    print(fin)
##    OutWords.draw(win)
##    x=len(fin)
##    OW= Text(Point(400,600),fin)
##    if x > 7:
##        OW.setSize(16)
##    if x<7 and x>5:
##        OW.setSize(18)
##    if x<5 and x>3:
##        OW.setSize(22)
##    if x<3:
##        OW.setSize(28)
##    OW.draw(win)
##    p=win.getMouse()
##    while not qb.isClicked(p):
##        p=win.getMouse()
##    win.close()
##
