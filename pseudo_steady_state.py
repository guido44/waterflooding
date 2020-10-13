import numpy as np
import pandas as pd
import math


def obtener_q(pwf, k, h, pr, uo, bo, re, rw, s):
    """
    Thi is a function to calculate the rates based on the pseudo-steady state Darcy equation
    :param pwf: Single-value or array of bottomhole pressures
    :param k: This is the effective permeability to the phase of analysis
    :param h: This is the reservoir thickness that contributes to the total flow
    :param pr: This is the average reservoir pressure
    :param uo: This is the viscosity of the phase under analysis
    :param bo: This is the formation volume factor
    :param re: This is the external boundary radius
    :param rw: This is the wellbore radius
    :param s: This is the skin factor
    :return: This will return a float if the pwf is a float or a np.array if pwf is an array
    """
    pwf = np.array(pwf)
    # Pseudo-steady state Darcy equation to calculate the rate of the analyzed phase
    q = (0.00708 * k * h * (pr - pwf)) / (uo * bo * (s - 0.75 + math.log(re / rw)))

    # Creation of result data
    result = {'rate': q, 'bottomhole pressure': pwf}
    dataframe = pd.DataFrame(result)
    return dataframe


print(obtener_q([1000], 10, 30, 2000, 10, 1.2, 500, 0.244, 3))