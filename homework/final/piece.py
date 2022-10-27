#all classes are identical in what functions they have,
#but each function differentiates
from grid import *

class Piece:
    def __init__(self, win, color):
        self.gwin = win
        self.color = color

#king
########################################################################################
class King(Piece):
    def __init__(self, win, color):
        self.gwin = win
        self.color = color
        if self.color == "black":
            self.k = Image(Point(1,1), "bking.gif")
        elif self.color == "white":
            self.k = Image(Point(1,1), "wking.gif")
        self.initPos()

    def returnPos(self):
        """returns the coordinates of the selected king"""
        return self.k.getAnchor()

    def returnColor(self):
        """returns the color of the selected king"""
        return self.color

    def initPos(self):
        """sets the initial position of the piece based on its color"""
        if self.color == "black":
            self.k.move(4,7)
            self.k.draw(self.gwin)
        elif self.color == "white":
            self.k.move(4,0)
            self.k.draw(self.gwin)

    def Captured(self):
        """removes the piece from the window"""
        self.k.undraw()

    def validMove(self, moveTo, pieces):
        """checks if the set move is a valid move, returns true or false"""
        x = self.returnPos().getX()
        y = self.returnPos().getY()
        x1 = moveTo[0]+1
        y1 = moveTo[1]+1
        if x+1 == x1 and y+1 == y1:
            return True
        if x+1 == x1 and y == y1:
            return True
        if x == x1 and y+1 == y1:
            return True
        if x-1 == x1 and y-1 == y1:
            return True
        if x-1 == x1 and y == y1:
            return True
        if x == x1 and y-1 == y1:
            return True
        if x-1 == x1 and y+1 == y1:
            return True
        if x+1 == x1 and y-1 == y1:
            return True
        return False

    def Move(self, pos):
        """moves the piece to the given coordinates"""
        x1 = self.returnPos().getX()
        y1 = self.returnPos().getY()
        x2 = pos[0]+1
        y2 = pos[1]+1
        self.k.move(x2-x1,y2-y1)

#queen
########################################################################################
class Queen(Piece):
    def __init__(self, win, color):
        self.gwin = win
        self.color = color
        if self.color == "black":
            self.q = Image(Point(1,1), "bqueen.gif")
        elif self.color == "white":
            self.q = Image(Point(1,1), "wqueen.gif")
        self.initPos()

    def returnPos(self):
        return self.q.getAnchor()

    def returnColor(self):
        return self.color

    def Captured(self):
        self.q.undraw()

    def validMove(self, moveTo, pieces):
        x = self.returnPos().getX()
        y = self.returnPos().getY()
        x1 = moveTo[0]+1
        y1 = moveTo[1]+1
        availableMoves = []

        #up right
        #############################
        #gets all of the available moves
        for i in range(8):
            #loops through all of the pieces on the board
            for piece in pieces:
                #set break to false, becasue we don't do it yet
                brake = False
                #get the location of the current piece
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                #if the piece is itself, just skip it 
                if x == xbad and y == ybad:
                    continue
                #if where we want to move has a piece there
                if xbad == x+i and ybad == y+i:
                    #add the move still if its opposite color - queen can take
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y+i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x+i, y+i))
                    #double break
                    brake = True
                    break
                
            #but if there isn't a piece there, add a piece
            availableMoves.append((x+i, y+i))
            #p much a method to double break
            if brake == True:
                break
        #right
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x+i and ybad == y:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x+i, y))
                    brake = True
                    break
                else:
                    availableMoves.append((x+i, y))
            if brake == True:
                break
        #up
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x and ybad == y+i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x, y+i))
                    brake = True
                    break
                else:
                    availableMoves.append((x, y+i))
            if brake == True:
                break
        #down left
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x-i and ybad == y-i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x-i, y-i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x-i, y-i))
                    brake = True
                    break
            availableMoves.append((x-i, y-i))
            if brake == True:
                break
        #left
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x-i and ybad == y:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x-i, y))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x-i, y))
                    brake = True
                    break
                else:
                    availableMoves.append((x-i, y))
            if brake == True:
                break
        #down
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x and ybad == y-i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x, y-i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x, y-i))
                    brake = True
                    break
                else:
                    availableMoves.append((x, y-i))
            if brake == True:
                break
        #down right
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x+i and ybad == y-i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y-i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x+i, y-i))
                    brake = True
                    break
                else:
                    availableMoves.append((x+i, y-i))
            if brake == True:
                break
        #up left
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x-i and ybad == y+i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x-i, y+i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x-i, y+i))
                    brake = True
                    break
                else:
                    availableMoves.append((x-i, y+i))
            if brake == True:
                break

        moves = []
        #gets rid of duplicates
        for i in availableMoves:
            if i not in moves:
                moves.append(i)
                
        #now loops through available moves for the piece
        for move in availableMoves:
            if x1 == move[0] and y1 == move[1]:
                return True
        

        return False


    def initPos(self):
        if self.color == "black":
            self.q.move(3,7)
            self.q.draw(self.gwin)
        elif self.color == "white":
            self.q.move(3,0)
            self.q.draw(self.gwin)

    def Move(self, pos):
        x1 = self.returnPos().getX()
        y1 = self.returnPos().getY()
        x2 = pos[0]+1
        y2 = pos[1]+1
        self.q.move(x2-x1,y2-y1)

#bishop
########################################################################################
class Bishop(Piece):
    def __init__(self, win, color, square):
        self.gwin = win
        self.color = color
        self.square = square
        if self.color == "black":
            self.b = Image(Point(1,1), "bbishop.gif")
        elif self.color == "white":
            self.b = Image(Point(1,1), "wbishop.gif")
        self.initPos()

    def returnPos(self):
        return self.b.getAnchor()

    def returnColor(self):
        return self.color

    def Captured(self):
        self.b.undraw()

    def validMove(self, moveTo, pieces):
        #just took everything from the queen that was valid
        x = self.returnPos().getX()
        y = self.returnPos().getY()
        x1 = moveTo[0]+1
        y1 = moveTo[1]+1
        availableMoves = []

        #up right
        #############################
        #gets all of the available moves
        for i in range(8):
            #loops through all of the pieces on the board
            for piece in pieces:
                #set break to false, becasue we don't do it yet
                brake = False
                #get the location of the current piece
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                #if the piece is itself, just skip it 
                if x == xbad and y == ybad:
                    continue
                #if where we want to move has a piece there
                if xbad == x+i and ybad == y+i:
                    #add the move still if its opposite color - queen can take
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y+i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x+i, y+i))
                    #double break
                    brake = True
                    break
                
            #but if there isn't a piece there, add a piece
            availableMoves.append((x+i, y+i))
            #p much a method to double break
            if brake == True:
                break

        #down left
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x-i and ybad == y-i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x-i, y-i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x-i, y-i))
                    brake = True
                    break
            availableMoves.append((x-i, y-i))
            if brake == True:
                break

        #down right
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x+i and ybad == y-i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y-i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x+i, y-i))
                    brake = True
                    break
                else:
                    availableMoves.append((x+i, y-i))
            if brake == True:
                break

        #up left
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x-i and ybad == y+i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x-i, y+i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x-i, y+i))
                    brake = True
                    break
                else:
                    availableMoves.append((x-i, y+i))
            if brake == True:
                break

        moves = []
        #gets rid of duplicates
        for i in availableMoves:
            if i not in moves:
                moves.append(i)
                
        #now loops through available moves for the piece
        for move in availableMoves:
            if x1 == move[0] and y1 == move[1]:
                return True
        
        return False


    def initPos(self):
        if self.color == "black":
            if self.square == "dark":
                self.b.move(2,7)
                self.b.draw(self.gwin)
            elif self.square == "light":
                self.b.move(5,7)
                self.b.draw(self.gwin)
        elif self.color == "white":
            if self.square == "dark":
                self.b.move(2,0)
                self.b.draw(self.gwin)
            elif self.square == "light":
                self.b.move(5,0)
                self.b.draw(self.gwin)

    def Move(self, pos):
        x1 = self.returnPos().getX()
        y1 = self.returnPos().getY()
        x2 = pos[0]+1
        y2 = pos[1]+1
        self.b.move(x2-x1,y2-y1)

#knight
########################################################################################
class Knight(Piece):
    def __init__(self, win, color, square):
        self.gwin = win
        self.color = color
        self.square = square
        if self.color == "black":
            self.n = Image(Point(1,1), "bknight.gif")
        elif self.color == "white":
            self.n = Image(Point(1,1), "wknight.gif")
        self.initPos()

    def returnPos(self):
        return self.n.getAnchor()

    def returnColor(self):
        return self.color

    def Captured(self):
        self.n.undraw()

    def validMove(self, moveTo, pieces):
        x = self.returnPos().getX()
        y = self.returnPos().getY()
        x1 = moveTo[0]+1
        y1 = moveTo[1]+1

        #dont need piece detection, because if opposite color, takes
        #if not opposite color, its already in the main func
        
        #two up one left
        if x-1 == x1 and y+2 == y1:
            return True
        #two up one right
        if x+1 == x1 and y+2 == y1:
            return True
        #one up two left
        if x-2 == x1 and y+1 == y1:
            return True
        #one up two right
        if x+2 == x1 and y+1 == y1:
            return True
        #one down two left
        if x-2 == x1 and y-1 == y1:
            return True
        #one down two right
        if x+2 == x1 and y-1 == y1:
            return True
        #two down one left
        if x-1 == x1 and y-2 == y1:
            return True
        #two down one right
        if x+1 == x1 and y-2 == y1:
            return True
        #if none above, return false
        return False

    def initPos(self):
        if self.color == "black":
            if self.square == "dark":
                self.n.move(1,7)
                self.n.draw(self.gwin)
            elif self.square == "light":
                self.n.move(6,7)
                self.n.draw(self.gwin)
        elif self.color == "white":
            if self.square == "dark":
                self.n.move(1,0)
                self.n.draw(self.gwin)
            elif self.square == "light":
                self.n.move(6,0)
                self.n.draw(self.gwin)

    def Move(self, pos):
        x1 = self.returnPos().getX()
        y1 = self.returnPos().getY()
        x2 = pos[0]+1
        y2 = pos[1]+1
        self.n.move(x2-x1,y2-y1)

#rook
########################################################################################
class Rook(Piece):
    def __init__(self, win, color, square):
        self.gwin = win
        self.color = color
        self.square = square
        if self.color == "black":
            self.r = Image(Point(1,1), "brook.gif")
        elif self.color == "white":
            self.r = Image(Point(1,1), "wrook.gif")
        self.initPos()

    def returnPos(self):
        return self.r.getAnchor()

    def returnColor(self):
        return self.color

    def Captured(self):
        self.r.undraw()

    def validMove(self, moveTo, pieces):
        #still just took the method from the queen
        x = self.returnPos().getX()
        y = self.returnPos().getY()
        x1 = moveTo[0]+1
        y1 = moveTo[1]+1
        availableMoves = []

        #right
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x+i and ybad == y:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x+i, y))
                    brake = True
                    break
                else:
                    availableMoves.append((x+i, y))
            if brake == True:
                break

        #up
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x and ybad == y+i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x+i, y))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x, y+i))
                    brake = True
                    break
                else:
                    availableMoves.append((x, y+i))
            if brake == True:
                break

        #left
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x-i and ybad == y:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x-i, y))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x-i, y))
                    brake = True
                    break
                else:
                    availableMoves.append((x-i, y))
            if brake == True:
                break

        #down
        #############################
        for i in range(8):
            for piece in pieces:
                brake = False
                xbad = piece.returnPos().getX()
                ybad = piece.returnPos().getY()
                if x == xbad and y == ybad:
                    continue
                if xbad == x and ybad == y-i:
                    if piece.returnColor() == "black" and self.returnColor()== "white":
                        availableMoves.append((x, y-i))
                    elif piece.returnColor() == "white" and self.returnColor()== "black":
                        availableMoves.append((x, y-i))
                    brake = True
                    break
                else:
                    availableMoves.append((x, y-i))
            if brake == True:
                break

        moves = []
        #gets rid of duplicates
        for i in availableMoves:
            if i not in moves:
                moves.append(i)
                
        #now loops through available moves for the piece
        for move in availableMoves:
            if x1 == move[0] and y1 == move[1]:
                return True
        return False


    def initPos(self):
        if self.color == "black":
            if self.square == "dark":
                self.r.move(0,7)
                self.r.draw(self.gwin)
            elif self.square == "light":
                self.r.move(7,7)
                self.r.draw(self.gwin)
        elif self.color == "white":
            if self.square == "dark":
                self.r.move(0,0)
                self.r.draw(self.gwin)
            elif self.square == "light":
                self.r.move(7,0)
                self.r.draw(self.gwin)

    def Move(self, pos):
        x1 = self.returnPos().getX()
        y1 = self.returnPos().getY()
        x2 = pos[0]+1
        y2 = pos[1]+1
        self.r.move(x2-x1,y2-y1)

#pawn
########################################################################################
class Pawn(Piece):
    def __init__(self, win, color, num):
        self.gwin = win
        self.num = num
        self.color = color
        if self.color == "black":
            self.p = Image(Point(1,1), "bpawn.gif")
        elif self.color == "white":
            self.p = Image(Point(1,1), "wpawn.gif")
        self.initPos()

    def returnPos(self):
        return self.p.getAnchor()

    def returnColor(self):
        return self.color

    def Captured(self):
        self.p.undraw()

    def validMove(self, moveTo, pieces):
        x = self.returnPos().getX()
        y = self.returnPos().getY()
        x1 = moveTo[0]+1
        y1 = moveTo[1]+1
        availableMoves = []
        
        for piece in pieces:
            xbad = piece.returnPos().getX()
            ybad = piece.returnPos().getY()
            if self.color == "black":
                #taking
                if x+1 == x1 and y-1 == y1:
                    return True
                if x-1 == x1 and y-1 == y1:
                    return True
                #100% case (unless taking)
                if x == xbad and y-1 == ybad:
                    return False
                #basic movement
                if x == x1 and y-1 == y1:
                    availableMoves.append((x1, y1))
                    #return True
                #pawn can double move if it is on first rank
                if y == 7:
                    if x == x1 and y-2 == y1:
                        #return True
                        availableMoves.append((x1, y1))
                    
            elif self.color == "white":
                #taking
                if x+1 == x1 and y+1 == y1:
                    return True
                if x-1 == x1 and y+1 == y1:
                    return True
                #100% case (unless taking)
                if x1 == xbad and y+1 == ybad:
                    return False
                #basic movement
                if x == x1 and y+1 == y1:
                    availableMoves.append((x1, y1))
                    #return True
                #pawn can double move if it is on first rank
                if y == 2:
                    if x == x1 and y+2 == y1:
                        #return True
                        availableMoves.append((x1, y1))

        moves = []
        #gets rid of duplicates
        for i in availableMoves:
            if i not in moves:
                moves.append(i)
                
        #now loops through available moves for the piece
        for move in availableMoves:
            if x1 == move[0] and y1 == move[1]:
                return True
        return False
                
        return False

    def initPos(self):
        if self.color == "black":
            if self.num == 1:
                self.p.move(0,6)
                self.p.draw(self.gwin)
            elif self.num == 2:
                self.p.move(1,6)
                self.p.draw(self.gwin)
            elif self.num == 3:
                self.p.move(2,6)
                self.p.draw(self.gwin)
            elif self.num == 4:
                self.p.move(3,6)
                self.p.draw(self.gwin)
            elif self.num == 5:
                self.p.move(4,6)
                self.p.draw(self.gwin)
            elif self.num == 6:
                self.p.move(5,6)
                self.p.draw(self.gwin)
            elif self.num == 7:
                self.p.move(6,6)
                self.p.draw(self.gwin)
            elif self.num == 8:
                self.p.move(7,6)
                self.p.draw(self.gwin)

        elif self.color == "white":
            if self.num == 1:
                self.p.move(0,1)
                self.p.draw(self.gwin)
            elif self.num == 2:
                self.p.move(1,1)
                self.p.draw(self.gwin)
            elif self.num == 3:
                self.p.move(2,1)
                self.p.draw(self.gwin)
            elif self.num == 4:
                self.p.move(3,1)
                self.p.draw(self.gwin)
            elif self.num == 5:
                self.p.move(4,1)
                self.p.draw(self.gwin)
            elif self.num == 6:
                self.p.move(5,1)
                self.p.draw(self.gwin)
            elif self.num == 7:
                self.p.move(6,1)
                self.p.draw(self.gwin)
            elif self.num == 8:
                self.p.move(7,1)
                self.p.draw(self.gwin)

    def Move(self, pos):
        x1 = self.returnPos().getX()
        y1 = self.returnPos().getY()
        x2 = pos[0]+1
        y2 = pos[1]+1
        self.p.move(x2-x1,y2-y1)
    
