"""
Collection of preset whitepoints in both 2 degree and 10 degree.
The exported shortcuts all reference the 2 degree standard obeserver
values.
"""


import numpy as np


CIE_1931_2_DEGREE_STD_OBSERVER = {
    'A':   [.44757, .40745],  # from Wikipedia
    'B':   [.34842, .35161],  # from Wikipedia
    'C':   [.31006, .31616],  # from Wikipedia
    'DCI': [.3140, .3510],    # Color & Mastering Digital Cinema
    'D50': [.34567, .35850],  # from Wikipedia
    'D55': [.33242, .34743],  # from Wikipedia
    'D60': [.32168, .33767],  # from github AMPAS/aces-dev
    'D65': [.31270, .32900],  # from github AMPAS/aces-dev
    'D75': [.29902, .31485],  # from Wikipedia
    'E':   [1/3, 1/3],        # From Wikipedia
}

CIE_1964_10_DEGREE_STD_OBSERVER = {
    'A':   [0.40745, 0.45117],  # from Wikipedia
    'B':   [0.34980, 0.35270],  # from Wikipedia
    'C':   [0.31039, 0.31905],  # from Wikipedia
    'D50': [0.34773, 0.35952],  # from Wikipedia
    'D55': [0.33411, 0.34877],  # from Wikipedia
    'D60': [0.32296, 0.33914],  # from colour-science.org
    'D65': [0.31382, 0.33100],  # from Wikipedia
    'D75': [0.29968, 0.31740],  # from Wikipedia
    'E':   [1/3, 1/3],          # from Wikipedia
}

def kelvin_to_xy_CIE_D(T):
    """ Convert Kelvin to CIE_D illuminant [x, y] """
    D_x = np.where(
        4000 <= T <= 7000,
        (-4.6070e9 / T ** 3) + (2.9678e6 / T ** 2) + (.09911e3 / T),
        (-2.0064e9 / T ** 3) + (1.9018e6 / T ** 2) + (.24748e3 / T))
    D_y = (-3.000 * D_x ** 2) + (2.870 * D_x) - .275
    return D_x, D_y
