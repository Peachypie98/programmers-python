from itertools import cycle
def solution(n):
    answer = ""
    for idx, i in enumerate(cycle('수박')):
        if(idx == n):
            break
        answer += i
    return answer