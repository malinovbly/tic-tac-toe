import os

from tictactoe import TicTacToe
from tictactoe.exceptions import CellException
from tictactoe.states import GameState


def game():
    app = TicTacToe()
    app.start()

    print("Tic-tac-toe\n")
    print("The coordinate format is 'xy', where x and y can be 1, 2, or 3")
    print("You always can exit with 'Ctrl + C'\n")
    input("Press Enter to start")

    while True:
        clear_console()
        print("The coordinate format is 'xy', where x and y can be 1, 2, or 3\n")
        print(app.board)
        command = input(f"Enter coordinates {app.player.name}: ")
        try:
            x, y = [int(i) for i in command]
            if len(command) == 2 and x in range(1, 4) and y in range(1, 4):
                try:
                    app.turn(y - 1, x - 1)
                except CellException as e:
                    invalid_coordinates()
                app.scan_board()
                check_game_state(app)
            else:
                invalid_coordinates()
        except ValueError:
            invalid_coordinates()


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def invalid_coordinates():
    input("Invalid coordinates (press Enter)")


def check_game_state(app: TicTacToe):
    game_state = app.state
    if game_state != GameState.PLAYING:
        clear_console()
        if game_state == GameState.X_WINS:
            print("X Wins\n")
        if game_state == GameState.O_WINS:
            print("O Wins\n")
        if game_state == GameState.DRAW:
            print("Draw\n")
        print(app.board)
        app.finish()
        input("Press enter to start new game")
        app.start()


if __name__ == "__main__":
    game()
