from ..entities import Board
from ..exceptions import GameStateException, GameStateExceptionMsg, CellException, CellExceptionMsg
from ..states import CellState, GameState, PlayerState


class TicTacToe:

    def __init__(self):
        self.__state = GameState.NOT_STARTED
        self.__player = PlayerState.X
        self.__board = Board()

    @property
    def state(self):
        return self.__state

    @property
    def player(self):
        return self.__player

    @property
    def board(self):
        return self.__board

    def finish(self):
        self.__init__()

    def start(self):
        if self.__state == GameState.PLAYING:
            raise GameStateException(GameStateExceptionMsg.GAME_ALREADY_STARTED)
        self.__state = GameState.PLAYING

    def pause(self):
        if self.__state == GameState.NOT_STARTED:
            raise GameStateException(GameStateExceptionMsg.GAME_NOT_STARTED)
        self.__state = GameState.PAUSED

    def x_wins(self):
        if self.__state == GameState.NOT_STARTED:
            raise GameStateException(GameStateExceptionMsg.GAME_NOT_STARTED)
        self.__state = GameState.X_WINS

    def o_wins(self):
        if self.__state == GameState.NOT_STARTED:
            raise GameStateException(GameStateExceptionMsg.GAME_NOT_STARTED)
        self.__state = GameState.O_WINS

    def draw(self):
        if self.__state == GameState.NOT_STARTED:
            raise GameStateException(GameStateExceptionMsg.GAME_NOT_STARTED)
        self.__state = GameState.DRAW

    def turn(self, x, y):
        if self.__state == GameState.NOT_STARTED:
            raise GameStateException(GameStateExceptionMsg.GAME_NOT_STARTED)
        cell = self.__board.get_cell(x, y)
        if cell.state != CellState.EMPTY:
            raise CellException(CellExceptionMsg.CELL_IS_NOT_EMPTY)
        if self.__player == PlayerState.X:
            cell.state = CellState.X
            self.__player = PlayerState.O
        else:
            cell.state = CellState.O
            self.__player = PlayerState.X

    def scan_board(self):
        if self.__state == GameState.NOT_STARTED:
            raise GameStateException(GameStateExceptionMsg.GAME_NOT_STARTED)
        grid = self.__board.grid
        lines = [sum(row) for row in grid]
        lines += [sum(col) for col in zip(*grid)]
        lines.append(sum(grid[i][i] for i in range(3)))
        lines.append(sum(grid[i][2 - i] for i in range(3)))
        if 3 in lines:
            self.x_wins()
        elif 30 in lines:
            self.o_wins()
        elif all(cell != 0 for row in grid for cell in row):
            self.draw()
