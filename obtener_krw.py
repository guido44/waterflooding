import numpy as np
import pandas as pd


def calculate_krw(swc, sor, krwmax, nw,  n):
    """
    This function calculates n values of Krw using the modified Brooks-Corey relations
    :param swc: This is the critical saturation of water
    :param sor: This is the residual saturation of oil
    :param krwmax: This is the maximum relative permeability for water between 0 and 1
    :param nw: This is the water exponent for modified Brooks-Corey relations range range from 1 to 6
    :param n: This is the number of rows calculated in the DataFrame
    :return: This will return a DataFrame with n Sw and Krw values
    """
    sw = np.linspace(swc, 1 - sor, n)
    # Modified Brooks-Corey relation for Krw
    krw = krwmax * ((sw - swc) / (1 - sor - swc)) ** nw
    # Creation of the result
    #result = {'Sw': sw, 'krw': krw}
    #dataframe = pd.DataFrame(result)
    return krw


#print(calculate_krw(0.363, 0.205, 1, 3, 20))