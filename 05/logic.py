from data_types import Rule, Update, List
from itertools import combinations
from functools import cmp_to_key

class OrderChecker:
    def __init__(self, rules: List[Rule]) -> None:
        largest = max(max(pair) for pair in rules)
        self.rule_matrix = [[0 for _ in range(largest+1)] for _ in range(largest+1)]
        for int1, int2 in rules:
            self.rule_matrix[int1][int2] = -1
            self.rule_matrix[int2][int1] = 1

    '''
    Returns true if int1 <= int2. False otherwise.
    '''
    def compare(self, int1: int, int2: int) -> int:
        return self.rule_matrix[int1][int2]

def solution1(rules: List[Rule], updates: List[Update]) -> int:
    total = 0
    order_checker = OrderChecker(rules)
    for update in updates:
        if is_correct(order_checker, update):
            total += middle_number(update)
    return total

def solution2(rules: List[Rule], updates: List[Update]) -> int:
    total = 0
    order_checker = OrderChecker(rules)
    order_key = cmp_to_key(lambda x,y: order_checker.compare(x,y))
    for update in updates:
        if not is_correct(order_checker, update):
            sorted_update = sorted(update, key=order_key)
            total += middle_number(sorted_update)
    return total

def is_correct(order_checker: OrderChecker, update: Update) -> bool:
    to_check = combinations(range(len(update)), 2)
    for id1, id2 in to_check:
        if order_checker.compare(update[id1], update[id2]) > 0:
            return False
    return True
    

def middle_number(update: Update) -> int:
    middle_index = len(update) // 2
    return update[middle_index]
