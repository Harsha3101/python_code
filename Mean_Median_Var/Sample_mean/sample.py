import numpy as np
def mat_mean(matrix):
    return np.mean(matrix, axis = None)
def mat_var(matrix):
    return np.var(matrix, axis = None)
def mat_std(matrix):
    k = np.std(matrix, axis = None)
    return k.round(11)
