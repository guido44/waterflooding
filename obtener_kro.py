import numpy as np
import pandas as pd


def calculate_kro(swc, sor, kromax, no,  n):
    """
    This function calculates n values of Kro using the modified Brooks-Corey relations
    :param swc: This is the critical saturation of water
    :param sor: This is the residual saturation of oil
    :param kromax: This is the maximum relative permeability for oil between 0 and 1
    :param no: This is the oil exponent for modified Brooks-Corey relations range range from 1 to 6
    :param n: This is the number of rows calculated in the DataFrame
    :return: This will return a DataFrame with n Sw and Kro values
    """
    sw = np.linspace(swc, 1 - sor, n)
    # Modified Brooks-Corey relation for Kro
    kro = kromax * ((1 - sw - sor) / (1 - sor - swc)) ** no
    # Creation of the result
    #result = {'Sw': sw, 'kro': kro}
    #dataframe = pd.DataFrame(result)
    return kro


#print(calculate_kro(0.363, 0.205, 1, 3, 20))