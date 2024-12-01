from read_input import read_input
from solution1 import total_distance

small_input_filename = "input_small"
small_input = (
    [3,4,2,1,3,3],
    [4,3,5,3,9,3],
)

assert(read_input(small_input_filename) == small_input)

assert(total_distance(*small_input) == 11)

assert(total_distance(*read_input(small_input_filename)) == 11)

print(total_distance(*read_input()))
