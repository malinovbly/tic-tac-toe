from enum import StrEnum


class GameStateExceptionMsg(StrEnum):
    GAME_NOT_STARTED = "Game isn't started"
    GAME_ALREADY_STARTED = "Game is already started"


class CellExceptionMsg(StrEnum):
    CELL_IS_NOT_EMPTY = "Cell isn't empty"
