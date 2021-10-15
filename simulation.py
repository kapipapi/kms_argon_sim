import numpy as np

from crystal import Crystal


def forces(c: Crystal, r: np.array):
    N, L, Eps, R, f = c.conf.N, c.conf.L, c.conf.Eps, c.conf.R, c.conf.f
    Vs = np.zeros(N)
    Vp = np.zeros(N)
    Fs = np.zeros((N, 3))
    Fp = np.zeros((N, 3))

    for i, r_i in enumerate(r):
        r_mod = np.linalg.norm(r_i)

        if r_mod > L:
            # siła od sfery
            Fs[i] = f * (L - r_mod) * r_i / r_mod

            # potencjał sfery
            Vs[i] = 0.5 * f * (r_mod - L) ** 2

        for j, r_j in enumerate(r[:i]):
            r_mod = np.linalg.norm(r_i - r_j)

            # potencjał van der vaalsa
            Vp[i] += Eps * ((R / r_mod) ** 12 - 2 * (R / r_mod) ** 6)

            # siła van der vaalsa
            Fp[i] += 12 * Eps * ((R / r_mod) ** 12 - (R / r_mod) ** 6) * (r_i - r_j) / r_mod ** 2
            Fp[j] -= 12 * Eps * ((R / r_mod) ** 12 - (R / r_mod) ** 6) * (r_i - r_j) / r_mod ** 2

    return np.sum(Vs) + np.sum(Vp), Fs + Fp, Fs