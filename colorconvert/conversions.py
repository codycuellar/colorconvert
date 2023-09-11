import numpy as np
from colorconvert.constants import PQ
from colorconvert.utils import cast_array


def RGB_to_XYZ(RGB, RGB_colorspace):
    RGB = cast_array(RGB)
    lin_rgb = RGB_colorspace.decode_tf(RGB.T)
    XYZ = np.dot(RGB_colorspace.M_matrix, lin_rgb).T
    return np.nan_to_num(XYZ)


def XYZ_to_RGB(XYZ, RGB_colorspace):
    XYZ = cast_array(XYZ)
    # Multiply inverse M-Matrix with XYZ
    rgb = np.dot(np.linalg.inv(RGB_colorspace.M_matrix), XYZ)
    # apply transfer function
    RGB = RGB_colorspace.encode_tf(rgb)
    return np.nan_to_num(RGB)


def RGB_to_RGB(RGB, input_RGB_colorpace, output_RGB_colorspace, normalize=False):
    XYZ = RGB_to_XYZ(RGB, input_RGB_colorpace)
    if normalize:
        max_ref_white_XYZ = max(xy_to_XYZ(input_RGB_colorpace.whitepoint))
        if max_ref_white_XYZ > 1:
            XYZ = XYZ * (1 / max_ref_white_XYZ)
    RGB = XYZ_to_RGB(XYZ, output_RGB_colorspace)
    return RGB


def xy_to_xyz(xy):
    x, y = xy
    z = 1.0 - x - y
    return cast_array([x, y, z])


def xyY_to_XYZ(xyY):
    x, y, Y = xyY
    if y == 0:
        return 0., 0., 0.
    X = (x * Y) / y
    Z = ((1 - x - y) * Y) / y
    return cast_array([X, Y, Z])


def xy_to_XYZ(xy):
    xyY = np.append(cast_array(xy), 1)
    XYZ = xyY_to_XYZ(xyY)
    return XYZ
