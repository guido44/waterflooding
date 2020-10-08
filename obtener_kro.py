import numpy as np
import pandas as pd


def obtener_kro(swi, sor, n):
    sw = np.linspace(swi, 1 - sor, n)
    swd = (sw - swi) / (1 - swi - sor)
    kro = ((1-swd)**2)*(1-swd**2)
    matriz_kro = np.array([sw, kro])
    dataframe1 = pd.DataFrame(matriz_kro)
    dataframe1 =dataframe1.T
    print(dataframe1)
    return kro

#print(obtener_kro(0.363, 0.205, 20))