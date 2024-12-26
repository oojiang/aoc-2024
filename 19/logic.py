from typing import List, Optional, Dict

def solution1(available: List[str], desired: List[str]) -> int:
    count = 0
    for pattern in desired:
        count += is_possible(available, pattern)
    return count

def solution2(available: List[str], desired: List[str]) -> int:
    count = 0
    cache = {}
    for pattern in desired:
        count += num_possible(available, pattern, cache)
    return count

def is_possible(available: List[str], desired_pattern: str) -> bool:
    seen = set()
    queue = []
    queue.append("")

    while queue:
        prefix = queue.pop()
        for pattern in available:
            next_prefix = prefix + pattern
            if next_prefix not in seen:
                if next_prefix == desired_pattern:
                    return True
                elif has_prefix(desired_pattern, next_prefix):
                    seen.add(next_prefix)
                    queue.append(next_prefix)
    
    return False

def num_possible(available: List[str], desired_pattern: str, cache: Optional[Dict] = None) -> int:
    if cache is not None and desired_pattern in cache:
        return cache[desired_pattern]

    if desired_pattern == "":
        if cache is not None:
            cache[desired_pattern] = 1
        return 1

    count = 0

    for prefix in available:
        if has_prefix(desired_pattern, prefix):
            count += num_possible(available, desired_pattern[len(prefix):], cache)

    if cache is not None:
        cache[desired_pattern] = count
    return count
    
def has_prefix(pattern: str, prefix: str) -> bool:
    return pattern[:len(prefix)] == prefix
