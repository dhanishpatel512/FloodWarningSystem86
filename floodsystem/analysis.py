import matplotlib
import numpy as np


def polyfit(dates, levels, p):
    """Returns a tuple (first entry: polynomial of degree p that best fits the data, second entry: shift in dates"""
    # Convert dates to floats
    x = matplotlib.dates.date2num(dates)

    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)

    return (poly, x[0])
