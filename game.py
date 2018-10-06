import board
import movement

class Game(redPlayer,blackPlayer):
	def __init__(self):
		self.redp = str(redPlayer)
		self.blkp = str(blackPlayer)
		self.redTurn = True

	#def takeTurn():
