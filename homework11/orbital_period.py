#file name: orbital period
import numpy as np

def orbital_period(a):
    """
    This function will calculate orbital period in years given the semi-major axis(a) in AU.
    """
    period = np.sqrt(a**3)
    return period
