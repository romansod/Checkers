import movement
import board
import game
def main():
    print("\n Welcome to Checkers\n")

    player1 = 'Roman'
    player2 = 'Lola'
    g = game.Game(board.Board(),player1,player2)
    while True:
        g.getBoard().print_board()
        g.takeTurn()


main()