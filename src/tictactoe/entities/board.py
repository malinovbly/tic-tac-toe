from .cell import Cell


class Board:

    def __repr__(self):
        res = ""
        for i in range(2, -1, -1):
            res += f"{self.get_cell(i, 0)} {self.get_cell(i, 1)} {self.get_cell(i, 2)}\n"
        return res

    def __init__(self):
        self.board = [[Cell(x, y) for y in range(3)] for x in range(3)]

    @property
    def grid(self):
        return [[self.get_cell(row, col).value for col in range(3)] for row in range(3)]

    def get_cell(self, x, y):
        return self.board[x][y]
