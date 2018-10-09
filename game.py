import board
import movement
from board import Occupant 
from movement import Direction

class Game:
    def __init__(self,board,redPlayer,blackPlayer):
        self.redp   = redPlayer
        self.blkp   = blackPlayer
        self.board  = board
        self.player = Occupant.BLACK
        self.movem  = movement.Movement()

    def getBoard(self):
        return self.board

    # Change who's turn it is
    def alternateTurn(self):
        if self.board.isSameColor(self.player,Occupant.RED):
            self.player = Occupant.BLACK
        else:
            self.player = Occupant.RED

    def print_player(self):
        player_name = ""
        if self.board.isSameColor(self.player,Occupant.RED):
            player_name = "\n--- RED PLAYER " + self.redp
        elif self.board.isSameColor(self.player,Occupant.BLACK):
            player_name = "\n- BLACK PLAYER " + self.blkp
        else:
            player_name = "\ngame.py:print_player():invalid player\n"

        print(player_name)

    def prompt_piece(self):
        while True:
            print("Please select a piece by it's coordinates")
            x = int(input("x: "))
            y = int(input("y: "))

            if self.board.isValidPieceSelection(self.player,x,y):
                pos = self.board.getPosition(x,y)
                v_directions = self.movem.getValidMoves(self.board,(x,y),pos)
                if len(v_directions) > 0:
                    return (x,y),v_directions

            print("That is not one of your pieces, please try again\n")

    # Parse input
    def input_direction(self,direction):
        if   direction == 'N':
            return Direction.NORTH
        elif direction == 'NE':
            return Direction.NORTHEAST
        elif direction == 'E':
            return Direction.EAST
        elif direction == 'SE':
            return Direction.SOUTHEAST
        elif direction == 'S':
            return Direction.SOUTH
        elif direction == 'SW':
            return Direction.SOUTHWEST    
        elif direction == 'W':
            return Direction.WEST
        elif direction == 'NW':
            return Direction.NORTHWEST
        return None

    def prompt_movement(self,piece,v_directions):
        while True:
            move = input("Select a direction of movement (N, NE, E ... etc):")
            move = self.input_direction(move)

            # Success:
            #      new_x, new_y, (ifJumpedx, ifJumpedy) or False
            #  Failure:
            #      None
            if move in v_directions:
                move_r = self.movem.Move(self.board, self.player, piece, move)

                if move_r:
                    return move_r
                
            print("Try moving piece <", piece,"> again")

    def resolve_turn_done(self, piece, move_xyj):
        # Place piece at new position and remove from older position
        self.board.setPosition(move_xyj[0],move_xyj[1],self.board.getPosition(piece[0],piece[1]))
        self.board.setPosition(piece[0],piece[1],Occupant.SPACE)

        jumped = move_xyj[2]

        # If an enemy piece was jumped, remove that piece and inform caller
        if jumped:
            self.board.setPosition(jumped[0],jumped[1],Occupant.SPACE)
            return True
        return False

    def takeTurn(self):
        # Print Playername and color
        self.print_player()

        # Prompt for piece selection
        while True:
            piece,v_directions = self.prompt_piece()
            if piece != None:
                break
            # TODO check if any valid moves for this piece
            print("prompt_piece: Something went wrong")
        
        pos = self.board.getPosition(piece[0],piece[1])
        # Prompt for movement
        while True:
            move_xyj = self.prompt_movement(piece,v_directions)
            if move_xyj == None:
                print("prompt_movement: Something went wrong")
                continue
                
            # Resolve consequences of turn
            if self.resolve_turn_done(piece, move_xyj):
                # If enemy piece claimed, prompt for another move if any moves available
                v_directions = self.movem.getValidMoves(self.board,piece,pos)
                if len(v_directions) > 0:
                    piece = move_xyj[0:2]
                    self.board.print_board()
                    continue    
            
            # Alternate player and return
            self.alternateTurn()
            return
            
