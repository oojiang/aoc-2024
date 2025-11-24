from typing import List
from state import read_input
from logic import RNG, Prices
from collections import deque

test_secrets = read_input("input2")
secrets = read_input()

def solution2(secrets: List[int]) -> int:
    total_price = {} # key = pattern, value = total price
    for i, secret in enumerate(secrets):
        print(i, secret)
        price_list = Prices(secret)
        seen = set()
        pattern = deque()
        for p, d in zip(price_list.prices, price_list.deltas):
            pattern.append(d)
            while len(pattern) > 4:
                pattern.popleft()
            tup = tuple(pattern)
            if len(tup) == 4 and tup not in seen:
                seen.add(tup)
                if tup not in total_price:
                    total_price[tup] = 0
                total_price[tup] += p

    return max(total_price.values())

assert(solution2(test_secrets) == 23)
print(solution2(secrets))
