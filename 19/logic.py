from typing import List

def solution1(available: List[str], desired: List[str]) -> int:
    count = 0
    for pattern in desired:
        count += is_possible(available, pattern)
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

def has_prefix(pattern: str, prefix: str) -> bool:
    return pattern[:len(prefix)] == prefix

