import numpy as np
import pandas as pd
import math


def obtener_q(k, h, pr, uo, bo, re, rw, s):
    pwf = np.linspace(0, pr, 10)
    q = (0.00708*k*h*(pr-pwf))/(uo*bo*(s-0.75+math.log(re/rw)))
    matriz_q = np.array([q, pwf])
    dataframe = pd.DataFrame(matriz_q)
    dataframe = dataframe.T
    from matplotlib import pyplot as plt
    plt.plot(q, pwf)
    plt.xlabel("q")
    plt.ylabel("pwf")
    plt.show()
    print("Tabla q y Pwf")
    return dataframe
#print(obtener_q(10, 30, 2000, 1, 1.2, 2000, 0.244, 1))