from obtener_kro import *
from obtener_krw import *


def calculate_fw(swc, sor, kromax, krwmax, no, nw, uo, uw, n):
    """
    This function calculates the fractional flow values using the relative permeabilities of the rock using the modified
    Brooks-Corey relations
    :param swc: This is the critical saturation of water
    :param sor: This is the residual saturation of oil
    :param kromax: This is the maximum relative permeability for oil between 0 and 1
    :param krwmax: This is the maximum relative permeability for water between 0 and 1
    :param no: This is the oil exponent for modified Brooks-Corey relations range range from 1 to 6
    :param nw: This is the water exponent for modified Brooks-Corey relations range range from 1 to 6
    :param uo: This is the oil viscosity given in cp
    :param uw: This is the water viscosity given in cp
    :param n: This is the number of rows calculated in the DataFrame
    :return: This will return a DataFrame with n Sw and fw values
    """
    sw = np.linspace(swc, 1 - sor, n)
    kro = calculate_kro(swc, sor, kromax, no, n)
    krw = calculate_krw(swc, sor, krwmax, nw, n)
    fw = 1 / (1 + ((kro * uw) / (krw * uo)))
    # Creation of the result
    result = {'Sw:': sw, 'fw:': fw}
    dataframe = pd.DataFrame(result)
    return dataframe


#print(calculate_fw(0.363, 0.205, 1, 1, 3, 3, 2, 1, 20))


