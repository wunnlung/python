#Todd Shriber, Gi Cortgrasso, project 5
#see READ_ME.txt

from graphics import *
from deck import *
from class_button import *
from game import *
from get_card import getCard





def main():
    #creating a window
    win = GraphWin("BlackJack", 800,800)
    #setting baclground to felt image
    #nvm it made the game too laggy so we're sticking to a green color
    background = Image(Point(400,400), "felt.gif")
    win.setBackground(color_rgb(8,61,22))
    #background.draw(win)
    #opening message
    welcome = Text(Point(400, 300), "Welcome to Todd's and Gi's Casino!")
    welcome.setSize(32)
    welcome.draw(win)
    
    #starting money count
    money = 100
    #gives the user the option to play again
    j=6
    time.sleep(2)
    welcome.undraw()
    while j == 6:
        #resets the background when clear
        mTxt = Text(Point(700,30), "Money:")
        mTxt.setSize(20)
        mTxt.draw(win)
        #actual count of money
        mCount = Text(Point(760, 30), money)
        mCount.setSize(20)
        mCount.draw(win)
        
    
        #input for bets
        inp = Entry(Point(400,400), 15)
        inp.draw(win)
        place_bets = Text(Point(400,375), "Place Your bet here:")
        place_bets.draw(win)
        #creating our start game button
        startGame = Button(win, Point(400,600),100,60, "Start?")
        p = win.getMouse()
        #while the button is not clicked, loop through until it is
        while not startGame.clicked(p):
            p = win.getMouse()
            
        #checks if input is a real number (loops until satisfied)
        while realNumber(inp.getText()) == False:
            wrong = Text(Point(400, 200), "Please Enter a Real Number")
            wrong.draw(win)
            #now needs the user to click again to recheck
            p = win.getMouse()
            while not startGame.clicked(p):
                p = win.getMouse()
            wrong.undraw()
            time.sleep(.5)
        
        
        #checks if user has enough funds (loops until satisfied)
        while int(inp.getText()) > money:
            invalid = Text(Point(400, 200), "Not Enough Funds")
            invalid.draw(win)
            p = win.getMouse()
            #then needs to click again
            while not startGame.clicked(p):
                p = win.getMouse()
            invalid.undraw()
            time.sleep(.5)
            #need to check if new number doesn't work either
            while realNumber(inp.getText()) == False:
                wrong = Text(Point(400, 200), "Please Enter a Real Number")
                wrong.draw(win)
                #now needs the user to click again to recheck
                p = win.getMouse()
                while not startGame.clicked(p):
                    p = win.getMouse()
                wrong.undraw()
                time.sleep(.5)

  
        #created an undraw function for the button
        startGame.undraw()
        #store the bet that the user did
        bet = int(inp.getText())
        #undrawing everything else
        place_bets.undraw()
        inp.undraw()
        
        #creates a deck for the game and shuffles
        gameDeck = Deck()
        gameDeck.shuffle()
        #creates the game
        playz = blackjack(gameDeck)
        #resets the game if there are previous games played
        playz.reset()
        #deals the initial cards
        playz.initDeal()

        #creating some things i can use later:
        game_over = Text(Point(400,300), "You Lose!")
        game_over.setSize(25)
        you_win = Text(Point(400,300), "You Win!")
        you_win.setSize(25)
        you_bust = Text(Point(400, 350), "You Bust")
        dealer_bust = Text(Point(400,350), "Dealer Bust")
        push = Text(Point(400,300), "Push!")
        push.setSize(25)
        go = Text(Point(400,300), "Game Over")
        go.setSize(32)
        
        #creates the hit and stand buttons
        hitButton = Button(win, Point(250,600), 100,60, "Hit")
        standButton = Button(win, Point(550,600), 100,60, "Stand")

        #total labels
        dealer_total = Text(Point(100,175), "Dealer:")
        player_total = Text(Point(100,425), "Player:")
        dealer_total.setSize(30)
        player_total.setSize(30)
        dealer_total.draw(win)
        player_total.draw(win)
        #get the value for the totals of the dealer
        dt = playz.evaluateHand("dealer")
        #create text line with that string
        #we can manipulate these later
        d = Text(Point(175,175), str(dt))
        d.setSize(30)
        d.draw(win)
        #now the player
        pt = playz.evaluateHand("player")
        #doing same thing
        if pt == "blackjack":
            p = Text(Point(225, 425), str(pt))
            p.setSize(30)
            p.draw(win)
        else:
            p = Text(Point(175,425), str(pt))
            p.setSize(30)
            p.draw(win)
        
        #prints the facedown card for dealer
        fdc = Image(Point(200,100), "b1fv.gif")
        fdc.draw(win)
        #sets a equal to the first dealer card
        a = playz.returnCard("dealer")
        #new string for creating image object
        card = ""
        #returnCard returns the cards as tuples in a list
        for i in a:
            card = getCard(i[0], i[1])
        #creates an image with the file name from above
        card_d1 = Image(Point(100,100), card)
        card_d1.draw(win)
        
        #print("")
        #print("you:")
        #now the player card
        b = playz.returnCard("player")
        #i will be our x coordinate so the images don't overlap
        i = 100
        #to differentiate the different cards
        n = 1
        for j in b:
            card = getCard(j[0], j[1])
            #creates image with coordinates i, 500
            card_player = Image(Point(i, 500), card)
            card_player.draw(win)
            #adds 100 to i for the next loop (new image)
            i+=100
            n+=1
            
    ####################################################################
            #player hit
        q = win.getMouse()
        #will loop through mouse clicks until stand button is pressed
        while not standButton.clicked(q):
            #if the hit button is clicked
            if hitButton.clicked(q):
                #function for hitting
                playz.hit("player")
                #doing the same method as before to print cards
                b = playz.returnCard("player")
                i = 100
                n=1
                for j in b:
                    card = getCard(j[0], j[1])
                    card_player = Image(Point(i, 500), card)
                    card_player.draw(win)
                    i+=100
                    n+=1
                #creates new text field for the total
                pt = playz.evaluateHand("player")
                p.undraw()
                #same thing
                if pt == "blackjack":
                    p = Text(Point(225, 425), str(pt))
                    p.setSize(30)
                    p.draw(win)
                else:
                    p = Text(Point(175,425), str(pt))
                    p.setSize(30)
                    p.draw(win)

                #seeing if the player loses to a bust
                #blackjack rules say that if player busts, they lose
                #even if dealer also busts
                if playz.evaluateHand("player") >= 22:
                    game_over.draw(win)
                    you_bust.draw(win)
                    #subtracts the bet from the user
                    money = money - bet
                    #resets the money count
                    mCount.undraw()
                    mCount = Text(Point(760, 30), money)
                    mCount.setSize(20)
                    mCount.draw(win)
                    #ends while loop if they bust
                    break
                else:
                    #get mouse again until the player hits stand
                    #or until they bust which is above
                    q = win.getMouse()

        #if the player has blackjack...
        if playz.evaluateHand("player") == "blackjack":
            #create blackjack text and draw it
            bj = Text(Point(400,300), "Blackjack!!")
            bj.setSize(30)
            bj.draw(win)
            bjBet = round(bet * 1.5)
            #add to the money count
            money += bjBet
            mCount.undraw()
            mCount = Text(Point(760, 30), money)
            mCount.setSize(20)
            mCount.draw(win)

            
        #only runs this if player didn't bust or got blackjack   
        elif playz.evaluateHand("player") <= 21:
            #runs the dealer
            run = playz.dealerplays(win, d)
            if run !=  "win" and run != "lose":
                if playz.evaluateHand("player")>playz.evaluateHand("dealer"):
                    you_win.draw(win)
                    money += bet
                    #resets the money count
                    mCount.undraw()
                    mCount = Text(Point(760, 30), money)
                    mCount.setSize(20)
                    mCount.draw(win)
                elif playz.evaluateHand("player")<playz.evaluateHand("dealer"):
                    game_over.draw(win)
                    money -= bet
                    #resets the money count
                    mCount.undraw()
                    mCount = Text(Point(760, 30), money)
                    mCount.setSize(20)
                    mCount.draw(win)
                else:
                    push.draw(win)
                    #keeps the money count the same
            #this will only happen if dealer gets blackjack
            elif run == "win":
                money -= bet
                #resets the money count
                mCount.undraw()
                mCount = Text(Point(760, 30), money)
                mCount.setSize(20)
                mCount.draw(win)
            elif run == "lose":
                money += bet
                #resets the money count
                mCount.undraw()
                mCount = Text(Point(760, 30), money)
                mCount.setSize(20)
                mCount.draw(win)
                
        #runs after round is over
        #undraws the hit and stand buttons        
        hitButton.undraw()
        standButton.undraw()            
        time.sleep(1)
        #if the player has no money, ends the game and quits
        if money <= 0:
            clear(win)
            go.draw(win)
            j = 7
            time.sleep(3)
            win.close()
            return None
        
            
        #gives the user the option to play another hand with their money
        restart = Text(Point(400,600), "Play Again?")
        restart.setSize(20)
        restart.draw(win)
        yes = Button(win, Point(250,600), 100,60, "Yes")
        no = Button(win, Point(550,600), 100,60, "No")
        pt = win.getMouse()
        #loops until the user clicks a button
        while not (no.clicked(pt) or yes.clicked(pt)):
            pt = win.getMouse()
        #if they select no, then end the program
        if no.clicked(pt):
            j = 7
            win.close()
        #if yes, loop back and have the user input another bet
        #(keep their total money from last hand)
        elif yes.clicked(pt):
            j = 6
            yes.undraw()
            no.undraw()
            #clears the entire window
            clear(win)
            
                
    
#method to remove all objects from the window
def clear(win):
    #for all items in the window
    for item in win.items[:]:
        #undraw everything
        item.undraw()
    #then update the window
    win.update()


#method to check if bet is an integer
def realNumber(inpput):
    #neat little thing to help (try/except)
    try:
        int(inpput)
    except ValueError:
        #return False if error is given
        return False
    #otherwise just return True
    return True





main()


