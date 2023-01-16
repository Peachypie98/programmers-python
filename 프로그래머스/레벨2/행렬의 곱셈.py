import numpy as np
def solution(arr1, arr2):
    arr1 = np.array(arr1, dtype = int)
    arr2 = np.array(arr2, dtype = int)
    answer = (arr1@arr2).tolist()
    return answer