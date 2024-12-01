from read_input import read_input
from solution2 import similarity_score

small_input_filename = "input_small"
small_input = (
    [3,4,2,1,3,3],
    [4,3,5,3,9,3],
)

assert(read_input(small_input_filename) == small_input)

assert(similarity_score(*small_input) == 31)

assert(similarity_score(*read_input(small_input_filename)) == 31)

print(similarity_score(*read_input()))

