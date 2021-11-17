class Config:
    def __init__(self, filename):
        inputData = open(filename, "r")
        self.n = int(inputData.readline())
        self.m = float(inputData.readline())
        self.a = float(inputData.readline())
        self.T_0 = float(inputData.readline())
        self.Eps = float(inputData.readline())
        self.L = float(inputData.readline())
        self.f = float(inputData.readline())
        self.R = float(inputData.readline())
        self.tau = float(inputData.readline())
        self.S_o = int(inputData.readline())
        self.S_d = int(inputData.readline())
        self.S_out = int(inputData.readline())
        self.S_xyz = int(inputData.readline())
        inputData.close()

        self.k = 8.31e-3

        self.N = self.n ** 3
