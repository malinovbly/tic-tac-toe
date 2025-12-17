from enum import Enum


class GameState(Enum):
    NOT_STARTED = 0
    PAUSED = 1
    PLAYING = 2
    X_WINS = 3
    O_WINS = 4
    DRAW = 5
