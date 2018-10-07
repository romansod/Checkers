import board
import movement

class Game(board,movement,redPlayer,blackPlayer):
	def __init__(self):
		self.redp   = "\n--- RED PLAYER (" + str(redPlayer) + ")"
		self.blkp   = "\n- BLACK PLAYER (" + str(blackPlayer) + ")"
		self.board  = board
		self.player = board.Occupant.RED

	def alternateTurn(self):
		self.player^=1

	def print_player(self):
		player_name = ""
		if self.player == board.Occupant.RED:
			player_name = self.redp
		elif self.player == board.Occupant.BLACK:
			player_name = self.blkp
		else:
			player_name = "\ngame.py:print_player():invalid player\n"

		print(player_name)

	def takeTurn():
		# Print Playername or color
		self.print_player()

		# Prompt for piece selection
		if board.isValidPieceSelection(self.player,x,y):
			
		# Prompt for movement
		# If either invalid, repeat
		# If enemy piece claimed, prompt for another move or none
		# Resolve consequences of turn
		# Alternate player and return
