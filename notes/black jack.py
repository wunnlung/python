#blackjack

from random import randrange


def main2():
    printIntro()
    n = int(input("How mnay times should I simulate the blackjack dealer?"))
    numBusted = simGames(n)
    print("He busted", numBusted/n*100, "percent of the time")

def printIntro():
    print("Welcome to a black jack simulator!")

def simGames(numTrials):
    totBusted = 0
    for i in range(numTrials):
        if dealerBusts():
            totBusted = totBusted + 1
    return totBusted

#simulate
def dealerBusts():
    points = 0 #initialize it to 0
    hasAce = False
    while points < 17:
        card = randrange(1,14)
        if card > 10:
            card = 10
        elif card == 1:
            hasAce = True
        points = points + card
        if hasAce and 17<= points + 10 <=21:
            points = points + 10
            
        
        
    if points > 21:
        return True
    else:
        return False
main2()





