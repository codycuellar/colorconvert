from __future__ import division
from typing import Union, List
import numpy as np
from colorconvert.constants import PQ


def srgb_to_lin(srgb_values):
    """
    Linearize sRGB tone curve.
    """
    return [np.where(
        v.T <= .04045,
        v.T / 12.92,
        np.power(((v.T + .055) / 1.055), 2.4)
    ) for v in srgb_values]


def lin_to_srgb(lin_values):
    """
    Encode sRGB tone curve from linear values.
    """
    return np.where(
        lin_values <=.0031308,
        lin_values * 12.92,
        1.055 * np.power(lin_values, 1 / 2.4) - .055
    )


def pq_to_lin(pq_values):
    """
    Linearize pq tone curve.
    """
    Nm2 = np.power(pq_values, (1 / PQ['m2']))
    return np.power(
        (Nm2 - PQ['c1']) / (PQ['c2'] - PQ['c3'] * Nm2),
        1 / PQ['m1']
    )


def lin_to_pq(lin_values):
    """
    Encode PQ tone curve from linear values.
    """
    Lm = np.power(lin_values, PQ['m1'])
    return np.power(
        (PQ['c1'] + PQ['c2'] * Lm) / (1 + PQ['c3'] * Lm),
        PQ['m2']
    )


def gamma_to_lin(gamma):
    return lambda gamma_values: np.power(gamma_values, gamma)


def lin_to_gamma(gamma):
    return lambda lin_values: np.power(lin_values, 1 / gamma)


def dci_to_lin(values):
    return gamma_to_lin(2.6)(values)


def lin_to_dci(values):
    return lin_to_gamma(2.6)(values)


def bt1886_to_lin(values):
    return gamma_to_lin(2.4)(values)


def lin_to_bt1886(values):
    return lin_to_gamma(2.4)(values)