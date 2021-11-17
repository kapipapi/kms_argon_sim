import time
import sys

import numpy as np
from crystal import Crystal
from init import generate_positions, generate_momentum
from simulation import forces

# kryształ (konfiguracja i baza)
c = Crystal(f"./data.txt")

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

T_avg = 0
P_avg = 0
H_avg = 0

frames = int(loops // c.conf.S_xyz)
outputData = open(f'./xyz.dat', "w")
outputData.write(f"{int(loops // c.conf.S_xyz)} {c.conf.N} {c.conf.tau} {c.conf.L}\n")

outputDatatHVTP = open(f'./out.dat', "w")
outputDatatHVTP.write(f"s\tt\tH\tV\tT\tP\n")

for s in range(loops):
    p = np.array([p_i + 0.5 * F_i * c.conf.tau for (p_i, F_i) in zip(p, F)])
    r = np.array([r_i + p_i * c.conf.tau / c.conf.m for (r_i, p_i) in zip(r, p)])
    V, F, Fs = forces(c, r)
    p = np.array([p_i + 0.5 * F_i * c.conf.tau for (p_i, F_i) in zip(p, F)])

    E_kin_tmp = [np.linalg.norm(p_i) ** 2 / (2 * c.conf.m) for p_i in p]
    P_tmp = sum([np.linalg.norm(Fs) ** 2 for Fs_i in Fs]) / (4 * np.pi * c.conf.L ** 2)

    if s % c.conf.S_out == 0:
        si = int(s / c.conf.S_out)
        print(si)
        outputDatatHVTP.write(f"{si}\t"
                              f"{s * c.conf.tau}\t"
                              f"{sum(E_kin_tmp) + V}\t"
                              f"{V}\t"
                              f"{2 * sum(E_kin_tmp) / (3 * c.conf.N * c.conf.k)}\t"
                              f"{P_tmp}\n")

    if s % c.conf.S_xyz == 0:
        for i, r_i in enumerate(r):
            outputData.write(f"{r_i[0]} {r_i[1]} {r_i[2]} {E_kin_tmp[i]}\n")
        outputData.write("\n\n")

    if s >= c.conf.S_o:
        T_avg += 2 * sum(E_kin_tmp) / (3 * c.conf.N * c.conf.k * c.conf.S_d)
        P_avg += P_tmp / c.conf.S_d
        H_avg += (sum(E_kin_tmp) + V) / c.conf.S_d

outputData.close()
outputDatatHVTP.close()
