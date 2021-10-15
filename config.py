class Config:
    inputData = open('data.txt', "r")
    n = int(inputData.readline())
    m = float(inputData.readline())
    a = float(inputData.readline())
    T_0 = float(inputData.readline())
    Eps = float(inputData.readline())
    L = float(inputData.readline())
    f = float(inputData.readline())
    R = float(inputData.readline())
    tau = float(inputData.readline())
    S_o = int(inputData.readline())
    S_d = int(inputData.readline())
    S_out = int(inputData.readline())
    S_xyz = int(inputData.readline())
    inputData.close()

    k = 8.31e-3

    N = n ** 3
