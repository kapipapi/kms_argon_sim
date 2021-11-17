import multiprocessing

from crystal import Crystal
from sim import simulation
from init import generate_positions

c = Crystal(f"./data.txt")
r = generate_positions(c)

processes = []

for T0 in range(500, 2500, 500):
    process = multiprocessing.Process(target=simulation, args=(r, c, T0))
    process.start()
    processes.append(process)

for t in processes:
    t.join()

print("Exiting Main Thread")
