from typing import Tuple
from enum import Enum

class Direction(Enum):
    UP      = (-1,  0)
    DOWN    = ( 1,  0)
    LEFT    = ( 0, -1)
    RIGHT   = ( 0,  1)

    def __init__(self, r: int, c: int) -> None:
        self.vec = (r, c)

    def move(self, r: int, c: int) -> Tuple[int, int]:
        r_ = r + self.vec[0]
        c_ = c + self.vec[1]
        return r_, c_
