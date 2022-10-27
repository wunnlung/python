#Todd Shriber, Gi Cortgrasso, project 5
#see READ_ME.txt

from deck import *
import random
from graphics import *
from get_card import getCard

class blackjack:
    def __init__(self, deck, dhand=[], phand = []):
        #just basic inits
        self.deck = deck
        self.dealer = dhand
        self.player = phand

    def initDeal(self):
        """gives dealer 1 card, and player 2 cards"""
        #gives the dealer 1 card
        self.dealer.append(self.deck.getCard(0))
        #gets rid of 1 card from the deck
        self.deck.dealtCard(1)
        #gives the player first 2 cards from dec k
        self.player.append(self.deck.getCard(0))
        self.player.append(self.deck.getCard(1))
        #removes the first 2 cards from deck
        self.deck.dealtCard(2)

    def evaluateHand(self, hand):
        """returns the total added up of an individual hand"""
        dtotal = 0
        ptotal = 0
        hasAce = False
        #a way to pick which hand to eval
        if hand == "dealer":
            for i in self.dealer:
                dtotal += i.getValue()[0]
                #checks if has ace card is true
                #if true, permamently sets ace to true for the hand
                if i.getValue()[1] == True:
                    hasAce = True
            #returns "blackjack" if all perameters are met
            if hasAce == True and dtotal == 21 and len(self.dealer) == 2:
                return "blackjack"
            #turns the ace into a 1 if dealer busts
            if hasAce == True and dtotal >= 22:
                dtotal = dtotal - 10
            #returns total value of dealaer hand if no blackjack
            return dtotal

        #does same thing for player hand instead
        elif hand == "player":
            for j in self.player:
                ptotal+= j.getValue()[0]
                #checks if has ace card is true
                #permanently sets has ace to true for the hand
                if j.getValue()[1] == True:
                    hasAce = True
            #returns "blackjack" if all perameters are met
            if hasAce == True and ptotal == 21 and len(self.player) == 2:
                return "blackjack"
            #turns the ace to a 1 if player buts
            if hasAce == True and ptotal >= 22:
                ptotal = ptotal - 10
            #returns total value of player hand if no blackjack
            return ptotal
        #don't need a final else because the player doesn't add or change code

    def showHand(self, hand):
        """shows the cards in an individual hand"""
        if hand == "dealer":
            for i in self.dealer:
                #shows each card in the dealer hand
                print(i)
        elif hand == "player":
            for j in self.player:
                #shows each card in the player hand
                print(j)
                
    def returnCard(self, hand):
        """returns the value and suit of the card in a tuple"""
        #overall same as show hand, but this returns values instead of printing
        cards = []
        if hand == "dealer":
            for i in self.dealer:
                cards.append(i.show())
        elif hand == "player":
            for j in self.player:
                cards.append(j.show())
        return cards
                

    def hit(self, hand):
        """adds a single card to a specified hand"""
        #hand is a method we used to not have to have seperate dealer hit and player hit
        if hand == "dealer":
            #adds the first card in the deck to the DEALER hand
            self.dealer.append(self.deck.getCard(0))
            #removes the first card in the deck
            self.deck.dealtCard(1)
        elif hand == "player":
            #adds the first card in the deck to the PLAYER hand
            self.player.append(self.deck.getCard(0))
            #removes the first card in the deck
            self.deck.dealtCard(1)

    def dealerplays(self, gwin, label):
        """runs the dealer hand until he gets over 16, or busts"""
        #this only ever runs if player doesn't bust or doesn't get blackjack
        #hits until over soft 16
        while int(self.evaluateHand("dealer")) <= 16:
            self.hit("dealer")
            #check for blackjack
            #if the length of the dealer hand is 2, then he can have blackjack
            if len(self.returnCard("dealer")) == 2:
                #if evalhand gives blackjack, give the game over stuff
                if self.evaluateHand("dealer") == "blackjack":
                    #wasn't showing the ace card, so do it here
                    i = 100
                    c = self.returnCard("dealer")
                    for k in c:
                        card = getCard(k[0], k[1])
                        card_dealer = Image(Point(i,100), card)
                        card_dealer.draw(gwin)
                        i+=100
                    #now print the game over text
                    #add a little time so it doesn't immediately say game over
                    time.sleep(1)
                    game_over = Text(Point(400,300), "You Lose!")
                    game_over.setSize(25)
                    blackjack = Text(Point(400, 350), "Dealer has Blackjack")
                    game_over.draw(gwin)
                    blackjack.draw(gwin)
                    #ends code if dealer has blackjack
                    return "win"
                       
                   
            #same method to draw the cards
            i = 100
            c = self.returnCard("dealer")
            
            for k in c:
                card = getCard(k[0], k[1])
                card_dealer = Image(Point(i, 100), card)
                card_dealer.draw(gwin)
                i += 100
            #changing the dealer count
            dt = self.evaluateHand("dealer")
            #undraw the old label (input from main)
            label.undraw()
            #create new text
            if dt == "blackjack":
                label = Text(Point(225, 175), str(dt))
                label.setSize(30)
                label.draw(win)
            else:
                label = Text(Point(175,175), str(dt))
                label.setSize(30)
                label.draw(gwin)
            #to add a little intensity to the game
            #so it doesn't finish right away
            time.sleep(1)

        #checks if dealer busts. If bust, prints you win
        if self.evaluateHand("dealer") >= 22:
            you_win = Text(Point(400,300), "You Win!")
            you_win.setSize(25)
            dealer_bust = Text(Point(400,350), "Dealer Bust")
            you_win.draw(gwin)
            dealer_bust.draw(gwin)
            #ends if dealer busts
            #returns that the dealer lost
            return "lose"
            #print("dealer busts!")
        #if no bust, print what they got (includes non blackjack 21)
        else:
            a = self.evaluateHand("dealer")
            #returns the exact value of the dealer to make things easier
            return a
            #return the actual value so we can interperit it in the code

    #experimental
    def reset(self):
        self.player = []
        self.dealer = []
            
            




##def testgame():
##    testDeck = Deck()
##    testDeck.shuffle()
##    tgame = blackjack(testDeck)
##    tgame.initDeal()
##    print("-----------")
##    tgame.hit("dealer")
##    tgame.dealerplays()
##    tgame.showHand("dealer")
##    
##
##        
##testgame()
