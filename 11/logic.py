from typing import List

def solution1(stones: List[int], n_blinks: int) -> int:
    return len(transform_n_times(stones, n_blinks))

def transform_n_times(stones: List[int], n_blinks: int) -> List[int]:
    for i in range(n_blinks):
        stones = transform(stones)
    return stones

def transform(stones: List[int]) -> List[int]:
    transformed_stones = []

    for n in stones:
        if n == 0:
            transformed_stones.append(1)
        elif len(str(n)) % 2 == 0:
            midpoint = len(str(n)) // 2
            left = int(str(n)[:midpoint])
            right = int(str(n)[midpoint:])
            transformed_stones.append(left)
            transformed_stones.append(right)
        else:
            transformed_stones.append(n * 2024)

    return transformed_stones
