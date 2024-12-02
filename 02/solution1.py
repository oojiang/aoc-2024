from typing import List
from itertools import pairwise

def num_safe_reports(reports: List[List[int]]) -> int:
    return sum(map(is_report_safe, reports))

def is_report_safe(report: List[int]) -> bool:
    # Reverse the order if needed so that we only need to check ascending.
    if report[0] < report[-1]:
        levels = iter(report)
    else:
        levels = reversed(report)

    # Check if all adjacent levels are safe.
    return all(is_safe(lvl1, lvl2) for lvl1, lvl2 in pairwise(levels))
    
# Checks if two adjacent levels are safe.
def is_safe(lvl1, lvl2):
    return lvl1 < lvl2 and lvl2 - lvl1 <= 3
    
