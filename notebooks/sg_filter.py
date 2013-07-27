# -*- coding: utf-8 -*-
# SciPy / Numpy implementation from the SciPy Cookbook; recipe implemented by Thomas Haslwanter
# http://www.scipy.org/Cookbook/SavitzkyGolay
#def savitzky_golay_1D(y, window_size, order, deriv=0, rate=1):
#    r"""Smooth (and optionally differentiate) data with a Savitzky-Golay filter.
#    The Savitzky-Golay filter removes high frequency noise from data.
#    It has the advantage of preserving the original shape and
#    features of the signal better than other types of filtering
#    approaches, such as moving averages techniques.
#
#    Parameters
#    ----------
#    y : array_like, shape (N,)
#        the values of the time history of the signal.
#    window_size : int
#        the length of the window. Must be an odd integer number.
#    order : int
#        the order of the polynomial used in the filtering.
#        Must be less then `window_size` - 1.
#    deriv: int
#        the order of the derivative to compute (default = 0 means only smoothing)
#
#    Returns
#    -------
#    ys : ndarray, shape (N)
#        the smoothed signal (or it's n-th derivative).
#    """
#    import numpy as np
#    from math import factorial
#
#    try:
#        window_size = np.abs(np.int(window_size))
#        order = np.abs(np.int(order))
#    except ValueError, msg:
#        raise ValueError("window_size and order have to be of type int")
#    if window_size % 2 != 1 or window_size < 1:
#        raise TypeError("window_size size must be a positive odd number")
#    if window_size < order + 2:
#        raise TypeError("window_size is too small for the polynomials order")
#    order_range = range(order+1)
#    half_window = (window_size -1) // 2
#    # precompute coefficients
#    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
#    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
#    # pad the signal at the extremes with
#    # values taken from the signal itself
#    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
#    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
#    y = np.concatenate((firstvals, y, lastvals))
#    return np.convolve( m[::-1], y, mode='valid')
    
def savitzky_golay_1D(y, window_size, order, deriv=0, rate=1):
    import numpy as np
    from math import factorial

    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')