import numpy as np

from crystal import Crystal


def generate_positions(c: Crystal) -> np.array:
    r_tmp = np.array([[0, 0, 0] for _ in range(c.conf.N)]).astype(float)
    for i_2 in range(c.conf.n):
        for i_1 in range(c.conf.n):
            for i_0 in range(c.conf.n):
                i = i_0 + i_1 * c.conf.n + i_2 * c.conf.n ** 2
                r_tmp[i] = \
                    (i_0 - (c.conf.n - 1) / 2) * c.b_0 + \
                    (i_1 - (c.conf.n - 1) / 2) * c.b_1 + \
                    (i_2 - (c.conf.n - 1) / 2) * c.b_2
    return r_tmp


def generate_momentum(c: Crystal, E_kin: np.array) -> np.array:
    p_tmp = np.zeros((c.conf.N, 3))
    for ii, (x, y, z) in enumerate(np.random.randint(2, size=(c.conf.N, 3)) * 2 - 1):
        p_tmp[ii] = \
            x * np.sqrt(2 * c.conf.m * E_kin[ii, 0]), \
            y * np.sqrt(2 * c.conf.m * E_kin[ii, 1]), \
            z * np.sqrt(2 * c.conf.m * E_kin[ii, 2])
    return p_tmp
