from grid import *
from piece import *
from csaudio import *
from wavmod import *


def main():
    win = GraphWin("hehe", 600, 600)
    win.setCoords(0, 0, 10,10)
    win.setBackground(color_rgb(208, 163, 115))
    board = Grid(win, 1, 1, 8, 8, 1, 1)
    board.setChessColor()
    pieces = []

    #sounds
    move_sound = WavMod("move.wav")
    take_sound = WavMod("take.wav")

    #kings
    bking = King(win, "black")
    pieces.append(bking)
    wking = King(win, "white")
    pieces.append(wking)

    #queens
    bqueen = Queen(win, "black")
    pieces.append(bqueen)
    wqueen = Queen(win, "white")
    pieces.append(wqueen)

    #bishops
    bbishopL = Bishop(win, "black", "light")
    pieces.append(bbishopL)
    bbishopD = Bishop(win, "black", "dark")
    pieces.append(bbishopD)
    wbishopL = Bishop(win, "white", "light")
    pieces.append(wbishopL)
    wbishopD = Bishop(win, "white", "dark")
    pieces.append(wbishopD)

    #knights
    bknightL = Knight(win, "black", "light")
    pieces.append(bknightL)
    bknightD = Knight(win, "black", "dark")
    pieces.append(bknightD)
    wknightL = Knight(win, "white", "light")
    pieces.append(wknightL)
    wknightD = Knight(win, "white", "dark")
    pieces.append(wknightD)

    #rooks
    brookL = Rook(win, "black", "light")
    pieces.append(brookL)
    brookD = Rook(win, "black", "dark")
    pieces.append(brookD)
    wrookL = Rook(win, "white", "light")
    pieces.append(wrookL)
    wrookD = Rook(win, "white", "dark")
    pieces.append(wrookD)

    #pawns
    for num in range(17):
        if num<9:
            bpawn = Pawn(win, "black", num)
            pieces.append(bpawn)
        else:
            wpawn = Pawn(win, "white", num-8)
            pieces.append(wpawn)


    #moving and game sim
    game_over = False
    #use same method as tiles to get turns
    turn = 1
    #loop until game over is True
    while game_over == False:
        #useful later for sounds
        t = False
        pt = win.getMouse()
        #gets the board pos of user click
        coord = board.getClickPos(pt)
        #set whose turn it is based on the turn #
        if turn%2 == 0:
            #black turn
            t = "black"
        elif turn%2 != 0:
            #white turn
            t = "white"
        #loops through pieces
        for i in pieces:
            #if person didnt click on board, leave for loop
            if coord == None:
                break
            #for every piece, get their x and y pos on board
            xcoor = i.returnPos().getX()
            ycoor = i.returnPos().getY()
            #if any piece has same pos as the mouseclick...
            if xcoor == coord[0]+1 and ycoor == coord[1]+1:
                #checks if the selected piece is the rigth color
                #still same turn because it doesn't get the chance
                #to move
                if t == "black":
                    if i.returnColor() != "black":
                        #break if color isn't black
                        break
                elif t == "white":
                    if i.returnColor() != "white":
                        #break is color isn't white
                        break
                #highlight that piece (selected)
                board.Highlight(pt)
                #get new mouse click
                pt2 = win.getMouse()
                #un-highlight the original piece
                board.unHighlight(pt)
                #gets the board pos of the second click
                moveTo = board.getClickPos(pt2)
                #if invalid move, don't move the piece
                if i.validMove(moveTo, pieces) == False:
                    break
                #if same pos as the original piece, leave for loop
                #(place piece back down)
                if moveTo == coord:
                    break
                #if new click isn't on the board, leave for loop
                elif moveTo == None:
                    break
                #if valid move...
                else:
                    #useful later
                    sameColor = False
                    #loop through remaining pieces
                    #not self, case happens above
                    for piece in pieces:
                        #get coordinates of each piece
                        x = piece.returnPos().getX()
                        y = piece.returnPos().getY()
                        #if the piece wants to move to a square that already
                        #has a piece, capture that piece
                        if x == moveTo[0]+1 and y == moveTo[1]+1:
                            if i.returnColor() == piece.returnColor():
                                sameColor = True
                                break
                                
                            else:
                                piece.Captured()
                                pieces.remove(piece)
                                sameColor = False
                                t = True
                            #leave this for loop so it doesn't use exrtra
                            #bandwidth
                            break
                    #actually move the original piece if not same color
                    if sameColor == True:
                        break
                    else:
                        i.Move(moveTo)
                        #if we took a piece, play take sound
                        if t == True:
                            take_sound.test()
                        #but if we didn't, play the move sound
                        else:
                            move_sound.test()
                        #now other turn
                        turn += 1
                        #leave the big for loop because we already found our
                        #piece and moved it
                        break
                
                
        
    




main()
