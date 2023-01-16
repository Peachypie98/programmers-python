def solution(array, commands):
    answer = []
    for A in commands:
        i,j,k = A
        tmp = sorted(array[i-1:j])
        answer.append(tmp[k-1])
    return answer