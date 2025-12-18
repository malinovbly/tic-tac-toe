import os

from tictactoe import TicTacToe
from tictactoe.exceptions import CellException
from tictactoe.states import GameState


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def invalid_coordinates():
    input("Invalid coordinates, press enter")


if __name__ == "__main__":
    game = TicTacToe()
    game.start()

    print("Tic-tac-toe\n")
    print("The coordinate format is 'xy', where x and y can be 1, 2, or 3")
    print("To quit the game, type 'quit'\n")
    input("Press enter to start")

    while True:
        clear_console()
        print(game.board)
        command = input(f"Enter coordinates {game.player.name}: ")
        if command == "quit":
            break
        try:
            x, y = [int(i) for i in command]
            if len(command) == 2 and x in range(1, 4) and y in range(1, 4):
                try:
                    game.turn(x - 1, y - 1)
                except CellException as e:
                    invalid_coordinates()
                game.scan_board()
                game_state = game.state
                if game_state != GameState.PLAYING:
                    clear_console()
                    print(game.board)
                    if game_state == GameState.X_WINS: print("X Wins")
                    if game_state == GameState.O_WINS: print("O Wins")
                    if game_state == GameState.NOT_STARTED: print("Draw")
                    game.finish()
                    input("Press enter to start new game")
                    game.start()
            else:
                invalid_coordinates()
        except ValueError:
            invalid_coordinates()
