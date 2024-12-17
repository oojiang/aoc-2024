from state import read_input, print_robots
from logic import move_robots, safety_factor
import matplotlib.pyplot as plt

RDIM = 103
CDIM = 101

safety_factors = []

# robots = read_input()
# for i in range(500):
#     safety_factors.append(safety_factor(robots, RDIM, CDIM))
#     robots = move_robots(robots, RDIM, CDIM)
#
# plt.plot(safety_factors)
# plt.show()

min_safety_factor = float('inf')
min_i = 0
robots = read_input()
for i in range(10000):
    i_safety_factor = safety_factor(robots, RDIM, CDIM)
    if i_safety_factor < min_safety_factor:
        min_safety_factor = i_safety_factor
        min_i = i
    robots = move_robots(robots, RDIM, CDIM)

print(min_i)

robots = read_input()
for _ in range(min_i):
    robots = move_robots(robots, RDIM, CDIM)
print_robots(robots, RDIM, CDIM)
    
