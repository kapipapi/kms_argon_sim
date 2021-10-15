import numpy as np

from config import Config


class Crystal:
    conf = Config()
    b_0 = np.array([conf.a, 0, 0])
    b_1 = np.array([conf.a / 2, conf.a * np.sqrt(3) / 2, 0])
    b_2 = np.array([conf.a / 2, conf.a * np.sqrt(3) / 6, conf.a * np.sqrt(2 / 3)])
