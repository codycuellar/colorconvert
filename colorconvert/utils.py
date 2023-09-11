from typing import List
import numpy as np


def cast_array(array: List) -> np.ndarray:
    if type(array) == np.ndarray:
        arr = array.astype(np.float32)
    else:
        arr = np.asarray(array, dtype=np.float32)
    return arr
