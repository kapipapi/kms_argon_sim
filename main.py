import numpy as np
import matplotlib.pyplot as plt

from crystal import Crystal
from init import generate_positions, generate_momentum
from simulation import forces
from graph import plot_positions, plot_momentum

# kryształ (konfiguracja i baza)
c = Crystal()

# położenia
r = generate_positions(c)
# plot_positions(r)

# energia kinetyczna
E_kin = np.array(-0.5 * c.conf.k * c.conf.T_0 * np.log(np.random.random(size=(c.conf.N, 3))))

# pędy
p = generate_momentum(c, E_kin)
p = p - sum(p) / c.conf.N
# plot_momentum(p)

V, F, Fs = forces(c, r)

# chwilowe ciśnienie na ścianki
pressure = sum(Fs) / (4 * np.pi * c.conf.L ** 2)

T = np.zeros(c.conf.S_o + c.conf.S_d)
T_avg = 0
P = np.zeros(c.conf.S_o + c.conf.S_d)
H = np.zeros(c.conf.S_o + c.conf.S_d)

for s in range(c.conf.S_o + c.conf.S_d):
    p = [p_i + 0.5 * F_i * c.conf.tau for (p_i, F_i) in zip(p, F)]
    r = [r_i + p_i * c.conf.tau / c.conf.m for (r_i, p_i) in zip(r, p)]

    V, F, Fs = forces(c, r)

    p = [p_i + 0.5 * F_i * c.conf.tau for (p_i, F_i) in zip(p, F)]

    T[s] = 2 * sum([np.linalg.norm(p_i) ** 2 / (2 * c.conf.m) for p_i in p]) / (3 * c.conf.N * c.conf.k)
    T_avg = sum(T) / c.conf.S_d

fig, ax = plt.subplots()
ax.plot(range(c.conf.S_o + c.conf.S_d), T)
plt.show()
