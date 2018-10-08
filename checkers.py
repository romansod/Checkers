import movement
import board
import game
def main():
    print("\n Welcome to Checkers\n")

    # b = board.Board()
    # b.print_board()
    # if b.isOnBoard(0,0):
    #     print('On Board')

    # if b.isRedPiece(0,0):
    #     print('RED')

    # if b.isRedPiece(7,0):
    #     print('RED')

    # m = movement.Movement()
    
    # print(m.Move(b,board.Occupant.BLACK,(1,0),movement.Direction.EAST))
    # print(m.Move(b,board.Occupant.RED,(1,0),movement.Direction.EAST))
    # print(m.Move(b,board.Occupant.RED,(6,3),movement.Direction.NORTHWEST))

    player1 = 'Roman'
    player2 = 'Lola'
    g = game.Game(board.Board(),player1,player2)
    while True:
        g.getBoard().print_board()
        g.takeTurn()


main()