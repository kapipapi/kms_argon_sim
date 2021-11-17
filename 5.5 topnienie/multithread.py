import multiprocessing
import time

from crystal import Crystal
from init import generate_positions
from sim import simulation

c = Crystal(f"./data.txt")
r = generate_positions(c)

processes = []

for T0 in range(0, 110, 10):
    process = multiprocessing.Process(target=simulation, args=(r, c, T0))
    process.start()
    processes.append(process)

for t in processes:
    t.join()

print("Exiting Main Thread")
