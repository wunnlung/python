#Todd Shriber, Gi Cortgrasso, project 5
#see READ_ME.txt

import random

class Card:
    def __init__(self, suit, value):
        #simple inits
        #was originally going to initialize all cards here
        #but it wasn't working
        #did it lower in deck class
        self.suit = suit #["Hearts", "Diamonds", "Spades", "Clubs"]
        self.value = value #["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]

    def getValue(self):
        """returns the value of the card"""
        a = self.value
        hasAce = False
        #if face card...
        if self.value == "Jack" or self.value == "Queen" or self.value == "King":
            #value is 10
            a = 10
        elif self.value == "Ace":
            #ace value is 11, and hasAce is true
            a = 11
            hasAce = True
        #return the value of the individual card, and if its an ace (bool)
        #this might seem useless, but it was very useful in the blackjack.py
        return (a,hasAce)

    def getSuit(self):
        """returns the suit of the card"""
        #just return the suit of the card
        return self.suit

    def show(self):
        """returns what your card is as a tuple"""
        #just returns the card as a tuple value
        s = self.suit
        v = self.value
        return (s,v)

    def __str__(self):
        """returns the card as a string"""
        #used to print, but needed it to return instead
        return str(self.value)+ " of "+ str(self.suit)


class Deck:
    def __init__(self):
        #basic inits you know you know
        self.Cards = []
        #NEVER MIND NOT BASIC HAHA
        #creates the actual deck
        self.create()

    def create(self):
        #called when deck object is created
        #loops through suits and values, making a deck of 52 cards
        suit = ["Hearts", "Diamonds", "Spades", "Clubs"]
        value = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
        for i in suit:
            for j in value:
                card = Card(i,j)
                self.Cards.append(card)

    def shuffle(self):
        """shuffles the deck"""
        #googled random for python and noticed this was a function
        return random.shuffle(self.Cards)

    def getCard(self, place):
        """returns the card at a specified place"""
        #self.Cards[place].show()
        return self.Cards[place]

    def removeCard(self, place):
        """remove card at specified place in the deck"""
        #just a simple pop command
        self.Cards.pop(place)

    def dealtCard(self, nCards):
        """remove n cards from the deck (input)"""
        #honestly don't remember if i used this or not
        #i may have only used the removeCard function above
        #but when we coded this I thought it seemed necessary
        for i in range(nCards):
            self.Cards.pop(0)
    
    def show(self):
        """prints out all the cards in the deck"""
        #this was useful for testing out stuff before I moved onto the graphics
        for i in self.Cards:
            i.show()

##def test():
##    #testCard = Card("Spades", "Ace")
##    #testCard.show()
##    #print(testCard)
##    #print("\n")
##    
##    testDeck = Deck()
##    #testDeck.show()
##    #print("\n")
##    testDeck.shuffle()
##    #testDeck.show()
##    #print("\n")
##    #testDeck.getCard(1)
##    testDeck.show()
##    print("\n")
##    testDeck.dealtCard(3)
##    testDeck.show()
##    
##
###test()
