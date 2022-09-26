import numpy as np


def floors(lists):
    array = np.array(lists)
    np.set_printoptions(legacy='1.13')
    return np.floor(array)
def ceils(lists):
    array = np.array(lists)
    return np.ceil(array)
def rints(lists):
    array = np.array(lists)
    return np.rint(array)

lists=[1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
k= floors(lists)