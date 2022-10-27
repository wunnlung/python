#Simulating the dealer in blackjack

## Needs minor modifications
## Triple pounds (###) indicate either:
##      1. that line was altered from the in-class version, or
##      2. you need to change something here for the lab

from random import *

def main():
    #print intro
    printIntro()
    #input num games to be simulated
    totalGames = eval(input("How many dealer hands do you want to simulate for each possible starting card?")) ###
    print ("The percentage of busted games for each possible starting card is as follows." )###
    ### for each possible starting card
    for startCard in range(1,14): ### this loop was not here before
        #simulate the blackjack dealer totalGames times and record how many times the dealer busted
        numBusted = simulateGames(totalGames, startCard) ### we are sending TWO arguments here now!
        #output summary of simulation results
        print(numBusted)
        print ( "For starting card " + str(startCard) + " bust percentage is "  + str(float(numBusted)/totalGames*100))
            
### Simulates the blackjack dealer n times for each possible starting card
### (Fix this function so that it has two parameters, as the call from the main function requires.)
def simulateGames(n, card):
    totalBustedGames = 0
    #do this n times:
    for i in range(n):
        ### Simulate game with the given initial showing card and see if dealer busts
        if dealerBusts(card): ### <-- this function call now needs an argument... what should you pass it?
            #add one to the total number of busted games
            totalBustedGames += 1
    return totalBustedGames

### Deals out one dealer-hand that starts with the given initialCard
# and returns True if dealer busts, False otherwise
def dealerBusts(initialCard): ### The initialcard parameter has been added
    if initialCard == 1:
        hasAce = True
    else:
    ### This is no longer necessarily the default initial value of hasAce,
    ### because the initialcard might be an Ace!  
        hasAce = False ### <-- so you need an if statement around this
    if initialCard > 10:
        points = 10
    else:
        points = initialCard
        
    ### This is also no longer initially true,
    ### since we now already have an initial card with some value...
    ### <-- so fix it!

    #keep dealing cards until total reaches 17
    while points < 17:
        card = randrange(1,14)
        if card > 10:
            card = 10
        elif card == 1:
            hasAce = True
        points = points + card
        if hasAce and 17<= points + 10 <=21:
            points = points + 10
        #everything else is the same as before...

    if points > 21:
        return True
    else:
        return False

    #...including the final if statement that goes here.
        
def printIntro():
    print ("This is a program that computes how often blackjack dealers bust.")
    print ("You input the number of times you want the simulation to be run.")
    print ("I output the percentage of times the dealer busts, for each initial dealer card. ") ###
    print ()

main()
