#returns the string of the file name for each card file
#need it to print cards in graphics window

def getCard(suit, value):
    if suit == "Hearts":
        if value == "Ace":
            return "h1.gif"
        elif value == 2:
            return "h2.gif"
        elif value == 3:
            return "h3.gif"
        elif value == 4:
            return "h4.gif"
        elif value == 5:
            return "h5.gif"
        elif value == 6:
            return "h6.gif"
        elif value == 7:
            return "h7.gif"
        elif value == 8:
            return "h8.gif"
        elif value == 9:
            return "h9.gif"
        elif value == 10:
            return "h10.gif"
        elif value == "Jack":
            return "h11.gif"
        elif value == "Queen":
            return "h12.gif"
        elif value == "King":
            return "h13.gif"
        
    elif suit == "Diamonds":
        if value == "Ace":
            return "d1.gif"
        elif value == 2:
            return "d2.gif"
        elif value == 3:
            return "d3.gif"
        elif value == 4:
            return "d4.gif"
        elif value == 5:
            return "d5.gif"
        elif value == 6:
            return "d6.gif"
        elif value == 7:
            return "d7.gif"
        elif value == 8:
            return "d8.gif"
        elif value == 9:
            return "d9.gif"
        elif value == 10:
            return "d10.gif"
        elif value == "Jack":
            return "d11.gif"
        elif value == "Queen":
            return "d12.gif"
        elif value == "King":
            return "d13.gif"

        
    elif suit == "Spades":
        if value == "Ace":
            return "s1.gif"
        elif value == 2:
            return "s2.gif"
        elif value == 3:
            return "s3.gif"
        elif value == 4:
            return "s4.gif"
        elif value == 5:
            return "s5.gif"
        elif value == 6:
            return "s6.gif"
        elif value == 7:
            return "s7.gif"
        elif value == 8:
            return "s8.gif"
        elif value == 9:
            return "s9.gif"
        elif value == 10:
            return "s10.gif"
        elif value == "Jack":
            return "s11.gif"
        elif value == "Queen":
            return "s12.gif"
        elif value == "King":
            return "s13.gif"

        
    elif suit == "Clubs":
        if value == "Ace":
            return "c1.gif"
        elif value == 2:
            return "c2.gif"
        elif value == 3:
            return "c3.gif"
        elif value == 4:
            return "c4.gif"
        elif value == 5:
            return "c5.gif"
        elif value == 6:
            return "c6.gif"
        elif value == 7:
            return "c7.gif"
        elif value == 8:
            return "c8.gif"
        elif value == 9:
            return "c9.gif"
        elif value == 10:
            return "c10.gif"
        elif value == "Jack":
            return "c11.gif"
        elif value == "Queen":
            return "c12.gif"
        elif value == "King":
            return "c13.gif"
