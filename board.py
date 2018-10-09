# Checkers

import sys
from colorama import Fore, Style, Back
from enum import Enum

class Occupant(Enum):
    SPACE   = 0
    BLACK   = 1
    RED     = 2
    BLACK_K = 3
    RED_K   = 4
    

PIECE = 'O'



class Board:
    def __init__(self):
        self.length = 8
        self.width  = 8
        self.grid   = [[Occupant.SPACE]*self.length for i in range(self.width)]
        # Grid is set to empty when initialized

        # Initialize Black pieces
        put_piece = False
        for y in range(self.length):
            for x in range(3):
                if put_piece:
                    self.grid[x][y] = Occupant.BLACK
                put_piece^=1

        # Initialize Red Pieces
        put_piece = True
        for y in range(self.length):    
            for x in range(5,8):
                if put_piece:
                    self.grid[x][y] = Occupant.RED
                put_piece^=1

    # Check validity of coordinates
    def isValidX(self,x):
        return 0 <= x and x < self.width 

    def isValidY(self,y):
        return 0 <= y and y < self.length 

    def isOnBoard(self,x,y):
        return self.isValidX(x) and self.isValidY(y)

    # Get and set what exists(if anything) at x y position
    def getPosition(self,x,y):
        return self.grid[x][y]

    def setPosition(self,x,y,occupant):
        self.grid[x][y] = occupant

    # Evaluate the board at position x y
    def isEmptySpace(self,pos):
        return pos == Occupant.SPACE

    def isBlackPiece(self,pos):
        return self.isSameColor(pos,Occupant.BLACK)

    def isRedPiece(self,pos):
        return self.isSameColor(pos,Occupant.RED)

    def isSameColor(self,color1,color2):
        if color1 == Occupant.SPACE or color2 == Occupant.SPACE:
            return False
        return (color1.value % 2) == (color2.value % 2)

    def isValidPieceSelection(self,color,x,y):
        if not self.isOnBoard(x,y):
            print('\nThat is not a valid board position\n')
            return False
        p = self.getPosition(x,y)
        if self.isEmptySpace(p):
            print('\nThere is no piece at that board position\n')
            return False
        if self.isSameColor(p,color) == False:
            print('\nYou must select one of your pieces\n')
            return False

        return True

    def canMoveHere(self,x,y):
        return self.isOnBoard(x,y) and self.isEmptySpace(self.getPosition(x,y))
    
    # Printing functions

    def print_space(self):
        print('   ', end='')

    def print_elem(self,x,y):
        pos = self.getPosition(x,y)
        print(Style.BRIGHT,end='')
        if self.isBlackPiece(pos):
            print(Fore.BLACK, end=' ')
            print(PIECE, end=' ')

        elif self.isRedPiece(pos):
            print(Fore.RED, end=' ')
            print(PIECE, end=' ')
        else:
            self.print_space()

        print(Fore.RESET, end='')

    # Sets the alternating space color
    def set_space(self, color_black):
        if color_black:
            print(Back.BLACK, end='')
        else:
            print(Back.RED, end='')

    # Prints the board and pieces
    def print_board(self):
        space_color = True
        for y in range(self.length-1,-1,-1):
            print(" ", y, end=' ')

            for x in range(self.width):
                self.set_space(space_color)
                space_color ^= 1
                self.print_elem(x,y)

            space_color ^= 1
            print(Style.RESET_ALL)

        self.print_space()
        print(end='  ')
        for i in range(self.width):
            print(i, end='  ')

        print()
    


