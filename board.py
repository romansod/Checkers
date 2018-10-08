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

        put_piece = False
        for y in range(self.length):
            for x in range(3):
                if put_piece:
                    self.grid[x][y] = Occupant.BLACK
                put_piece^=1

        put_piece = True
        for y in range(self.length):    
            for x in range(5,8):
                if put_piece:
                    self.grid[x][y] = Occupant.RED
                put_piece^=1

    def isValidX(self,x):
        return 0 <= x and x < self.width 

    def isValidY(self,y):
        return 0 <= y and y < self.length 

    def isOnBoard(self,x,y):
        return self.isValidX(x) and self.isValidY(y)

    def isEmptySpace(self,x,y):
        return self.getPosition(x,y) == Occupant.SPACE

    def getPosition(self,x,y):
        return self.grid[x][y]

    def setPosition(self,x,y,occupant):
        self.grid[x][y] = occupant

    def isBlackPiece(self,x,y):
        p = self.getPosition(x,y)
        return p == Occupant.BLACK or p == Occupant.BLACK_K

    def isRedPiece(self,x,y):
        p = self.getPosition(x,y)
        return p == Occupant.RED or p == Occupant.RED_K

    def isSameColor(self,color1,color2):
        if color1 == Occupant.SPACE or color2 == Occupant.SPACE:
            return False
        return (color1.value % 2) == (color2.value % 2)

    def isValidPieceSelection(self,color,x,y):
        if not self.isOnBoard(x,y):
            print('\nThat is not a valid board position\n')
            return False

        if self.isEmptySpace(x,y):
            print('\nThere is no piece at that board position\n')
            return False
        p = self.getPosition(x,y)
        if self.isSameColor(p,color) == False:
            print('\nYou must select one of your pieces\n')
            return False

        return True

    def canMoveHere(self,x,y):
        return self.isOnBoard(x,y) and self.isEmptySpace(x,y)
    
    # Printing functions

    def print_space(self):
        print('   ', end='')

    def print_elem(self,x,y):
        print(Style.BRIGHT,end='')
        if self.isBlackPiece(x,y):
            print(Fore.BLACK, end=' ')
            print(PIECE, end=' ')

        elif self.isRedPiece(x,y):
            print(Fore.RED, end=' ')
            print(PIECE, end=' ')
        else:
            self.print_space()

        print(Fore.RESET, end='')

    def set_space(self, color_black):
        if color_black:
            print(Back.BLACK, end='')
        else:
            print(Back.RED, end='')

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
    


