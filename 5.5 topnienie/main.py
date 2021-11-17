from crystal import Crystal
from init import generate_positions
from topnienie.sim import simulation

c = Crystal(f"./data.txt")
r = generate_positions(c)

for T0 in range(0, 1000, 100):
    simulation(r, c, T0)
