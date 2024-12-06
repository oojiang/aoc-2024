from typing import Tuple, List, TypeAlias
from enum import Enum

class Direction(Enum):
    UP      = (-1,  0)
    DOWN    = ( 1,  0)
    LEFT    = ( 0, -1)
    RIGHT   = ( 0,  1)

    def __init__(self, x, y):
        self.vec = (x, y)

    def turn(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        else:
            return Direction.UP

    def symbol(self):
        if self == Direction.UP:
            return "^"
        elif self == Direction.RIGHT:
            return ">"
        elif self == Direction.LEFT:
            return "<"
        else:
            return "v"


Map: TypeAlias = List[List[str]]
Position: TypeAlias = Tuple[int, int]
IsOnMap: TypeAlias = bool
State: TypeAlias = Tuple[IsOnMap, Position, Direction]

