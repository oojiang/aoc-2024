from read_input import read_input
from solution2 import num_safe_reports_with_dampen, is_report_safe_with_dampen

small_input_filename = "input_small"
small_input = [
    [7,6,4,2,1],
    [1,2,7,8,9],
    [9,7,6,2,1],
    [1,3,2,4,5],
    [8,6,4,4,1],
    [1,3,6,7,9],
]

assert(read_input(small_input_filename) == small_input)

assert(is_report_safe_with_dampen(small_input[0]) == True)
assert(is_report_safe_with_dampen(small_input[1]) == False)
assert(is_report_safe_with_dampen(small_input[2]) == False)
assert(is_report_safe_with_dampen(small_input[3]) == True)
assert(is_report_safe_with_dampen(small_input[4]) == True)
assert(is_report_safe_with_dampen(small_input[5]) == True)

assert(num_safe_reports_with_dampen(small_input) == 4)

assert(num_safe_reports_with_dampen(read_input(small_input_filename)) == 4)

print(num_safe_reports_with_dampen(read_input()))
