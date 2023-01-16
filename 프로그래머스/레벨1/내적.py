import numpy as np
def solution(a, b):
    a = np.array(a, dtype = int)
    b = np.array(b, dtype = int)
    return a.dot(b).tolist()