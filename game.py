import board
import movement

class Game(board,redPlayer,blackPlayer):
	def __init__(self):
		self.redp   = "\n--- RED PLAYER (" + str(redPlayer) + ")"
		self.blkp   = "\n- BLACK PLAYER (" + str(blackPlayer) + ")"
		self.board  = board
		self.player = board.Occupant.RED

	def alternateTurn(self):
		self.player^=1

	def print_player(self):
		player_name = ""
		if self.player == self.board.Occupant.RED:
			player_name = self.redp
		elif self.player == self.board.Occupant.BLACK:
			player_name = self.blkp
		else:
			player_name = "\ngame.py:print_player():invalid player\n"

		print(player_name)

	def prompt_piece(self):
		while True:
			print("Please select a piece by it's coordinates")
			x = input("x: ")
			y = input("y: ")

			if self.board.isValidPieceSelection(self.player,x,y):
				return x,y
			else:
				print("That is not one of your pieces, please try again\n")

	def prompt_movement(self,piece):
		m = movement.Movement()

		while True:
			move = input("Select a direction of movement (N, NE, E ... etc):")
			
			# Success:
  			#      new_x, new_y, ifJumped
    		#  Failure:
    		#	   None
       
			move_r = m.Move(self.board, self.player, piece, move):
			if move_r:
				return move_r
        	print("Try moving piece <", piece,"> again")

	def takeTurn():
		# Print Playername or color
		self.print_player()

		# Prompt for piece selection
		piece = self.prompt_piece()
		if piece == None:
			print("prompt_piece: Something went wrong")
			return

		# Prompt for movement
		move = prompt_movement(piece)
		if move == None:
			print("prompt_movement: Something went wrong")
			return
			
		# If either invalid, repeat
		# If enemy piece claimed, prompt for another move or none
		# Resolve consequences of turn
		# Alternate player and return
