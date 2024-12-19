from typing import Tuple, TypeAlias
from enum import Enum

Coor: TypeAlias = Tuple[int, int]

class Direction(Enum):
    UP      = (-1,  0)
    DOWN    = ( 1,  0)
    LEFT    = ( 0, -1)
    RIGHT   = ( 0,  1)

    def __init__(self, x, y):
        self.vec = (x, y)

    def index(self):
        if self == Direction.UP:
            return 0
        elif self == Direction.DOWN:
            return 1
        elif self == Direction.LEFT:
            return 2
        else:
            return 3

    def turn_clockwise(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        else:
            return Direction.UP

    def turn_counterclockwise(self):
        if self == Direction.UP:
            return Direction.LEFT
        elif self == Direction.RIGHT:
            return Direction.UP
        elif self == Direction.DOWN:
            return Direction.RIGHT
        else:
            return Direction.DOWN

    def move(self, coor: Coor) -> Coor:
        r = coor[0] + self.vec[0]
        c = coor[1] + self.vec[1]
        return (r, c)

    def symbol(self):
        if self == Direction.UP:
            return "^"
        elif self == Direction.RIGHT:
            return ">"
        elif self == Direction.LEFT:
            return "<"
        else:
            return "v"

State: TypeAlias = Tuple[Coor, Direction]
