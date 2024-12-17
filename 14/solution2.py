from state import read_input, print_robots
from logic import move_robots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print_robots(read_input("input1"), 7, 11)
RDIM = 103
CDIM = 101

# i = 0
# robots = read_input()
# print("ELAPSED TIME:", i)
# print_robots(robots, RDIM, CDIM)
# print()
#
# while True:
#     i += 1
#     robots = move_robots(robots, RDIM, CDIM)
#     if True:
#         input()
#         print("ELAPSED TIME:", i)
#         print_robots(robots, RDIM, CDIM)
#         print()

x_stdevs = []
y_stdevs = []

robots = read_input()
for i in range(500):
    x_pos = [robot[0][0] for robot in robots]
    y_pos = [robot[0][1] for robot in robots]
    x_std = np.std(x_pos)
    y_std = np.std(y_pos)
    x_stdevs.append(x_std)
    y_stdevs.append(y_std)
    robots = move_robots(robots, RDIM, CDIM)

plt.plot(x_stdevs)
plt.plot(y_stdevs)
plt.show()

# The first x-anomaly occurs at 19, and the first y-anomaly occurs at 70.
# The x-anomalies have a period of 103, while the y-anomalies have a period of 101.
# Thus, we're looking for values of x and y that satisfy: 19 + 103x = 70 + 101y.
# This is a diophantine equation and we can solve using the euclidean algorithm. My math is quite rusty, so I am going to brute force it with grid search instead.

answer = -1
for x in range(100):
    for y in range(100):
        if 19 + 103 * x == 70 + 101 * y:
            print(x, y)
            answer = 19 + 103 * x
            print(answer)

# Smallest solution is (76, 77)
# So, the first time step should be 19 + 103 * 76 = 70 + 101 * 77 = 7847

robots = read_input()
for _ in range(answer):
    robots = move_robots(robots, RDIM, CDIM)
print_robots(robots, RDIM, CDIM)
