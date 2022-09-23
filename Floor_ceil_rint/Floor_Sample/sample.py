import numpy as np


def floors(lists):
    array = np.array(lists)
    np.set_printoptions(legacy='1.13')
    return np.floor(array)
def ceils(lists):
    array = np.array(lists)
    np.set_printoptions(legacy='1.13')
    return np.ceil(array)
def rints(lists):
    array = np.array(lists)
    np.set_printoptions(legacy='1.13')
    return np.rint(array)