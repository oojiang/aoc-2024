from typing import List
from solution1 import is_safe, is_report_safe

def num_safe_reports_with_dampen(reports: List[List[int]]) -> int:
    return sum(map(is_report_safe_with_dampen, reports))

def is_report_safe_with_dampen(report: List[int]) -> bool:
    # Reverse the order if needed so that we only need to check ascending.
    if report[0] < report[-1]:
        levels = list(iter(report))
    else:
        levels = list(reversed(report))

    # dynamic programming to check if the report is safe with dampening.
    queue = [(0, 1, 0)]
    while queue:
        curr_id, next_id, num_dampened = queue.pop()

        if num_dampened >= 2:
            continue

        if curr_id < 0:
            queue.append((next_id, next_id + 1, num_dampened))
            continue

        if next_id >= len(levels):
            return True

        if is_safe(levels[curr_id], levels[next_id]):
            queue.append((next_id, next_id + 1, num_dampened))
        else:
            queue.append((curr_id - 1,  next_id,        num_dampened + 1))
            queue.append((curr_id,      next_id + 1,    num_dampened + 1))

    return False

def num_safe_reports_with_dampen_naive(reports: List[List[int]]) -> int:
    return sum(map(is_report_safe_with_dampen_naive, reports))

def is_report_safe_with_dampen_naive(report: List[int]) -> bool:
    if is_report_safe(report):
        return True
    else:
        dampened_reports = []
        for i in range(len(report)):
            dampened_report = report.copy()
            dampened_report.pop(i)
            dampened_reports.append(dampened_report)

        return any(map(is_report_safe, dampened_reports))
