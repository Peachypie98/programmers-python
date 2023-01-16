def solution(n, i = 0):
    answer = [x for x in range(2, 999999) if n % x  == 1][0]
    return answer