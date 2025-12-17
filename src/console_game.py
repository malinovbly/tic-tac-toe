from src.tictactoe import TicTacToe
from src.tictactoe.exceptions import CellException
from src.tictactoe.states import GameState

if __name__ == "__main__":
    game = TicTacToe()
    game.start()

    print("Tic-tac-toe")
    print(game.board)
    print("The coordinate format is 'xy', where x and y can be 1, 2, or 3")
    print("To quit the game, enter 'quit'")
    while True:
        command = input(f"Enter coordinates {game.player.name}: ")
        if command == "exit":
            break
        try:
            x, y = [int(i) for i in command]
            if len(command) == 2 and x in range(1, 4) and y in range(1, 4):
                try:
                    game.turn(x-1, y-1)
                except CellException as e:
                    print("Invalid coordinates")
                    continue
                game.scan_board()
                game_state = game.state
                print(game.board, "\n")
                if game_state != GameState.PLAYING:
                    if game_state == GameState.X_WINS:
                        print("X Wins")
                    if game_state == GameState.O_WINS:
                        print("O Wins")
                    if game_state == GameState.NOT_STARTED:
                        print("Draw")
                    game.finish()
                    break
            else:
                print("Invalid coordinates")
        except ValueError:
            print("Invalid coordinates")
