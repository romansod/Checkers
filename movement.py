import board
from enum import Enum
from board import Occupant

class Direction(Enum):
    NORTH     = 0
    NORTHEAST = 1
    EAST      = 2
    SOUTHEAST = 3
    SOUTH     = 4
    SOUTHWEST = 5
    WEST      = 6
    NORTHWEST = 7

red   = {Direction.NORTHWEST,Direction.SOUTHWEST}
black = {Direction.NORTHEAST,Direction.SOUTHEAST}
king  = {Direction.EAST,Direction.WEST}

class Movement:
    
    def N(self,x,y):
        return x  ,y+1

    def NE(self,x,y):
        return x+1,y+1

    def E(self,x,y):
        return x+1,y

    def SE(self,x,y):
        return x+1,y-1

    def S(self,x,y):
        return x  ,y-1

    def SW(self,x,y):
        return x-1,y-1

    def W(self,x,y):
        return x-1,y

    def NW(self,x,y):
        return x-1,y+1

    def setDirection(self,direction):
        if   direction == Direction.NORTH:
            return self.N
        elif direction == Direction.NORTHEAST:
            return self.NE
        elif direction == Direction.EAST:
            return self.E
        elif direction == Direction.SOUTHEAST:
            return self.SE
        elif direction == Direction.SOUTH:
            return self.S
        elif direction == Direction.SOUTHWEST:
            return self.SW
        elif direction == Direction.WEST:
            return self.W
        elif direction == Direction.NORTHWEST:
            return self.NW
        return None


    def move_set(self,board,color):
        if board.isSameColor(color,Occupant.RED):
            if color == Occupant.RED_K:
                return red.union(king)
            return red
        elif board.isSameColor(color,Occupant.BLACK):
            if color == Occupant.BLACK_K:
                return black.union(king)
            return black
            
    def getValidMoves(self,board,piece,color):
        all_moves = self.move_set(board,color)
        actual_moves = set()
        for d in all_moves:
            step = self.setDirection(d)
            x,y = step(piece[0],piece[1])
            
            if board.isOnBoard(x,y):
                pos = board.getPosition(x,y)
                if pos == Occupant.SPACE:
                    actual_moves.add(d)
                    continue
                if board.isSameColor(color,pos) == False:
                    x,y = step(x,y)
                    if board.canMoveHere(x,y):
                        actual_moves.add(d)
                        continue
        return actual_moves

    """
    All movements return the following:
    
    Success:
        new_x, new_y, ifJumped

    Failure:
        None
    """

    def Move(self,board,color,piece,direction):
        p = board.getPosition(piece[0],piece[1])
        if board.isSameColor(p,color) == False:
            return None

        step = self.setDirection(direction)

        if step == None:
            print("No valid direction was specified")
            return None

        print(piece[0],piece[1])
        x,y = step(piece[0],piece[1])
        print(x,y)

        if board.isOnBoard(x,y) == False:
            return None
        np = board.getPosition(x,y)
        if board.isEmptySpace(np):
            return x,y,False

        if board.isSameColor(np,color) == False:
            # Jump and take piece
            nx,ny = step(x,y)

            if board.canMoveHere(nx,ny):
                return nx,ny,(x,y)
            else:
                return None

        return None

    

