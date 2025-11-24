from typing import List
from state import read_input
from logic import RNG

def solution1(secrets: List[int]):
    total = 0
    for secret in secrets:
        r = RNG(secret)
        for _ in range(2000):
            r.evolve()
        total += r.secret
    return total

test_secrets = read_input("input1")
secrets = read_input()

assert(solution1(test_secrets) == 37327623)
print(solution1(secrets))
