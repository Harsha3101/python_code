import numpy as np
def min_max(k):
    l=sorted(np.min(k, axis = 1))
    return l[-1]
