import numpy as np
import pandas as pd
import math
from obtener_kro import *
from obtener_krw import *


def obtener_fw(swi, sor, uo, uw, n):
    sw = np.linspace(swi, 1 - sor, n)
    print("Tabla Kro")
    kro = obtener_kro(swi, sor, n)
    print("Tabla Krw")
    krw = obtener_krw(swi, sor, n)
    fw = 1/(1+((kro*uw)/(krw*uo)))
    matriz_fw = np.array([sw,fw])
    dataframe = pd.DataFrame(matriz_fw)
    dataframe = dataframe.T
    from matplotlib import pyplot as plt
    plt.plot(sw, fw)
    plt.xlabel("Sw")
    plt.ylabel("fw")
    plt.show()
    print("Tabla fw")
    return dataframe

#print(obtener_fw(0.365, 0.205, 2, 1, 20))


