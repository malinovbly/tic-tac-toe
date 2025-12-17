from ..states import CellState, GameState


class Cell:

    def __repr__(self):
        if self.__state == CellState.EMPTY:
            return f"-"
        return f"{self.__state.name}"

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__state = CellState.EMPTY

    @property
    def position(self):
        return self.__x, self.__y

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, new_state):
        self.__state = new_state

    @property
    def value(self):
        return self.__state.value

    def set_x(self):
        self.__state = CellState.X

    def set_o(self):
        self.__state = CellState.O

    def set_empty(self):
        self.__state = CellState.EMPTY
