import time
import sys

import numpy as np
from crystal import Crystal
from init import generate_positions, generate_momentum
from simulation import forces

c = Crystal(f"./data.txt")
outputData = open(f'./V(a).dat', "w")

for i in range(350, 401, 1):
    c.conf.a = i / 1000
    c.b_0 = np.array([c.conf.a, 0, 0])
    c.b_1 = np.array([c.conf.a / 2, c.conf.a * np.sqrt(3) / 2, 0])
    c.b_2 = np.array([c.conf.a / 2, c.conf.a * np.sqrt(3) / 6, c.conf.a * np.sqrt(2 / 3)])
    r = generate_positions(c)
    V, _, _ = forces(c, r)
    outputData.write(f"{c.conf.a}\t{V}\n")
outputData.close()
