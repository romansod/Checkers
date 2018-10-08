import board
from enum import Enum

class Direction(Enum):
    NORTH     = 0
    NORTHEAST = 1
    EAST      = 2
    SOUTHEAST = 3
    SOUTH     = 4
    SOUTHWEST = 5
    WEST      = 6
    NORTHWEST = 7

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

        if board.isEmptySpace(x,y):
            return x,y,False

        np = board.getPosition(x,y)

        if board.isSameColor(np,color) == False:
            # Jump and take piece
            nx,ny = step(x,y)

            if board.canMoveHere(nx,ny):
                return nx,ny,(x,y)
            else:
                return None

        return None

    

