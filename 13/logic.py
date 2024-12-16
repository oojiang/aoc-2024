from typing import List, Tuple, TypeAlias
from sympy import Matrix

Vector: TypeAlias = Tuple[int, int]

def solution1(machines: List[Tuple[Vector, Vector, Vector]]) -> int:
    tokens = 0
    for vec_a, vec_b, prize in machines:
        count_a, count_b = get_strategy(vec_a, vec_b, prize)
        tokens += 3 * count_a + 1 * count_b
    return tokens

def solution2(machines: List[Tuple[Vector, Vector, Vector]]) -> int:
    tokens = 0
    for vec_a, vec_b, prize in machines:
        count_a, count_b = get_strategy(vec_a, vec_b, convert_prize(prize))
        tokens += 3 * count_a + 1 * count_b
    return tokens

def convert_prize(prize: Vector) -> Vector:
    c = 10000000000000
    return (prize[0] + c, prize[1] + c)

def get_strategy(vec_a: Vector, vec_b: Vector, prize: Vector) -> Vector:
    basis = Matrix([
        [vec_a[0], vec_b[0]],
        [vec_a[1], vec_b[1]]
    ]).inv()
    
    vector = Matrix([
        [prize[0]],
        [prize[1]]
    ])

    result = basis * vector

    is_fractional = any(element.denominator > 1 for element in result)

    if is_fractional:
        return (0, 0)
    else:
        return (result[0], result[1])
