from colorconvert.colorspaces import RGBColorSpace
from colorconvert import gamuts
from colorconvert.whitepoints import CIE_1931_2_DEGREE_STD_OBSERVER as wp
from colorconvert import transfer_functions as tf


DISPLAY_COLORSPACES = {
    'sRGB_D65': RGBColorSpace(gamuts.sRGB, wp['D65'], tf.lin_to_srgb, tf.srgb_to_lin, name='sRGB D65'),
    'REC709': RGBColorSpace(gamuts.BT709, wp['D65'], tf.lin_to_bt1886, tf.bt1886_to_lin, name='BT709'),
    'P3_PQ_D65': RGBColorSpace(gamuts.P3, wp['D65'], tf.lin_to_pq, tf.pq_to_lin, name='P3 PQ D65'),
    'P3_DCI': RGBColorSpace(gamuts.P3, wp['DCI'], tf.lin_to_dci, tf.dci_to_lin, name='P3 DCI'),
}
