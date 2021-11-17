import numpy as np

from config import Config


class Crystal:
    def __init__(self, filename):
        self.conf = Config(filename)
        self.b_0 = np.array([self.conf.a, 0, 0])
        self.b_1 = np.array([self.conf.a / 2, self.conf.a * np.sqrt(3) / 2, 0])
        self.b_2 = np.array([self.conf.a / 2, self.conf.a * np.sqrt(3) / 6, self.conf.a * np.sqrt(2 / 3)])
