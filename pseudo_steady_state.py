import numpy as np
import pandas as pd
import math


def calculate_q(pwf, k, h, pr, uo, bo, re, rw, s, pb):
    """
    Thi is a function to calculate the rates based on the pseudo-steady state Darcy equation and the Vogel equation
    :param pwf: Single-value or array of bottomhole pressures
    :param k: This is the effective permeability to the phase of analysis
    :param h: This is the reservoir thickness that contributes to the total flow
    :param pr: This is the average reservoir pressure
    :param uo: This is the viscosity of the phase under analysis
    :param bo: This is the formation volume factor
    :param re: This is the external boundary radius
    :param rw: This is the wellbore radius
    :param s: This is the skin factor
    :param pb: This is the bubble point pressure
    :return: This will return a float if the pwf is a float or a np.array if pwf is an array
    """

    pwf = np.array(pwf)
    # pwfd is an array with all the values of pressure that are greater than the bubble point pressure
    pwfd = pwf > pb
    # pwfv is an array with all the values of pressure that are lees than or equal the bubble point pressure
    pwfv = pwf <= pb

    # %%
    # Pseudo-steady state Darcy equation to calculate the rate of the analyzed phase when
    # the bottomhole pressure is greater than the bubble point pressure

    # qd is an array with the rates when the bottomhole pressure is greater than the bubble point pressure
    qd = (0.00708 * k * h * (pr - pwf[pwfd])) / (uo * bo * (s - 0.75 + math.log(re / rw)))

    # %%
    # Vogel equation to calculate the rate of the analyzed phase when the bottomhole pressure is less than the bubble
    # point pressure

    # qb means the rate calculated at the bubble point pressure
    qb = (0.00708 * k * h * (pr - pb)) / (uo * bo * (s - 0.75 + math.log(re / rw)))
    # qomax is the maximum rate when the bottomhole pressure is 0
    qomax = qb / (1 - 0.2 * (pb/pr) - 0.8 * (pb/pr) ** 2)
    # qv is an array with the rates when the bottomhole pressure is less than the bubble point pressure
    qv = qomax * (1 - 0.2 * (pwf[pwfv]/pr) - 0.8 * (pwf[pwfv]/pr) ** 2)
    # %%

    # Creation of result data
    q = np.concatenate((qd,qv))
    result = {'rate': q, 'bottomhole pressure': pwf}
    dataframe = pd.DataFrame(result)
    return dataframe


#print(calculate_q([3200, 3000, 2800, 2000, 1800, 1000, 200, 0],30, 30, 3200, 1.2, 1.2, 2000, 0.244, 2, 1800))