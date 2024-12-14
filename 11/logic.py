from typing import List, Dict

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

def solution2(stones: List[int], n_blinks: int) -> int:
    stones_count = transform_fast_n_times(count_stones(stones), n_blinks)

    return sum(stones_count.values())

def count_stones(stones: List[int]) -> Dict[int, int]:
    stones_count = {}
    for n in stones:
        if n not in stones_count:
            stones_count[n] = 0
        stones_count[n] += 1
    return stones_count


def transform_fast_n_times(stones: Dict[int, int], n_blinks: int) -> Dict[int, int]:
    for i in range(n_blinks):
        stones = transform_fast(stones)
    return stones

def transform_fast(stones: Dict[int, int]) -> Dict[int, int]:
    transformed_stones = {}

    for n in stones:
        for m in transform([n]):
            if m not in transformed_stones:
                transformed_stones[m] = 0
            transformed_stones[m] += stones[n]

    return transformed_stones
        
