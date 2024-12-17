from typing import List, Tuple, Iterable, TypeAlias
from itertools import product
from functools import reduce
import operator

Vector: TypeAlias = Tuple[int, int]
Robot: TypeAlias = Tuple[Vector, Vector]

RDIM = 103
CDIM = 101

ELAPSED_TIME = 100

def solution1(robots: List[Robot], rdim: int = RDIM, cdim: int = CDIM) -> int:
    for _ in range(ELAPSED_TIME):
        robots = move_robots(robots, rdim, cdim)
    return safety_factor(robots, rdim, cdim)

def move_robots(robots: List[Robot], rdim: int, cdim: int) -> List[Robot]:
    new_robots = []
    for robot in robots:
        new_robots.append(move_robot(robot, rdim, cdim))
    return new_robots

def move_robot(robot: Robot, rdim: int, cdim: int) -> Robot:
    position, velocity = robot
    xpos, ypos = position
    xvel, yvel = velocity

    new_position = (
        (xpos + xvel) % cdim, 
        (ypos + yvel) % rdim
    )

    return (new_position, velocity)

def safety_factor(robots: List[Robot], rdim: int, cdim: int) -> int:
    top =       range(0,            rdim//2)
    bottom =    range(rdim//2 + 1,  rdim)
    left =      range(0,            cdim//2)
    right =     range(cdim//2 + 1,  cdim)
    quadrants = list(product([left, right], [top, bottom]))
    counts = [0] * len(quadrants)
    for robot in robots:
        for i in range(len(quadrants)):
            if robot_in_quadrant(robot, quadrants[i]):
                counts[i] += 1
    return reduce(operator.mul, counts)

def robot_in_quadrant(robot: Robot, quadrant: Tuple[Iterable, Iterable]) -> bool:
    position, _ = robot
    xpos, ypos = position

    xrange, yrange = quadrant

    return (xpos in xrange) and (ypos in yrange)
