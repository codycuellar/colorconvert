from ctypes import cast
import numpy as np
from colorconvert.conversions import xy_to_xyz, xy_to_XYZ
from colorconvert import whitepoints as wp, gamuts, transfer_functions as tf, constants
from colorconvert.utils import cast_array

class RGBColorSpace:

    def __init__(self, gamut, whitepoint, encode_tf, decode_tf, name=''):
        self.name = name
        self.whitepoint = cast_array(whitepoint)
        self.primaries = cast_array(gamut)
        self.decode_tf = decode_tf
        self.encode_tf = encode_tf
        self.M_matrix = self.calc_matrix()

    def calc_matrix(self):
        rgb_xyz = cast_array(list(map(xy_to_xyz, self.primaries)))
        ref_white_XYZ = xy_to_XYZ(self.whitepoint)
        rgb_XYZ_sums = np.dot(ref_white_XYZ, np.linalg.inv(rgb_xyz))
        return np.dot(rgb_xyz.transpose(), np.diagflat(rgb_XYZ_sums))
