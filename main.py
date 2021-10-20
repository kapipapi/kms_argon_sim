import time

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

# simulation
loops = c.conf.S_o + c.conf.S_d
set_size = int(loops / c.conf.S_out)

t_set = np.zeros(set_size)
H_set = np.zeros(set_size)
V_set = np.zeros(set_size)
T_set = np.zeros(set_size)
P_set = np.zeros(set_size)

T_avg = 0
P_avg = 0
H_avg = 0

frames = int(loops//c.conf.S_xyz)
outputData = open(f'avs_{frames}frames_{time.time()}.dat', "w")
outputData.write(f"{int(loops//c.conf.S_xyz)} {c.conf.N}\n")

for s in range(loops):
    p = np.array([p_i + 0.5 * F_i * c.conf.tau for (p_i, F_i) in zip(p, F)])
    r = np.array([r_i + p_i * c.conf.tau / c.conf.m for (r_i, p_i) in zip(r, p)])
    V, F, Fs = forces(c, r)
    p = np.array([p_i + 0.5 * F_i * c.conf.tau for (p_i, F_i) in zip(p, F)])

    E_kin_tmp = [np.linalg.norm(p_i) ** 2 / (2 * c.conf.m) for p_i in p]

    if s % c.conf.S_out == 0:
        si = int(s / c.conf.S_out)
        print(si)
        t_set[si] = s * c.conf.tau
        H_set[si] = sum(E_kin_tmp) + V
        V_set[si] = V
        T_set[si] = 2 * sum(E_kin_tmp) / (3 * c.conf.N * c.conf.k)
        P_set[si] = sum([np.linalg.norm(Fs) ** 2 for Fs_i in Fs]) / (4 * np.pi * c.conf.L ** 2)

    if s % c.conf.S_xyz == 0:
        for i, r_i in enumerate(r):
            outputData.write(f"{r_i[0]} {r_i[1]} {r_i[2]} {E_kin_tmp[i]}\n")
        outputData.write("\n\n")

    if s >= c.conf.S_o:
        T_avg += 2 * sum(E_kin_tmp) / (3 * c.conf.N * c.conf.k * c.conf.S_d)
        # P_avg = P_avg.append()
        # H_avg = H_avg.append()

    print(f"loop {s}/{loops}")

outputData.close()
