import numpy as np
import pandas as pd


def obtener_krw(swi, sor, n):
    sw = np.linspace(swi, 1 - sor, n)
    swd = (sw - swi) / (1 - swi - sor)
    krw = swd ** 4
    matriz_krw = np.array([sw, krw])
    dataframe1 = pd.DataFrame(matriz_krw)
    dataframe1 =dataframe1.T
    print(dataframe1)
    return krw

#print(obtener_krw(0.363, 0.205, 20))