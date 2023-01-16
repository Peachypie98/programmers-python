def solution(arr1, arr2):
    answer = arr2.copy()
    for idx, i in enumerate(arr1):
        for idx2, x in enumerate(i):
            answer[idx][idx2] += x
    return answer