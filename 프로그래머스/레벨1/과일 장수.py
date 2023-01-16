def solution(k, m, score):
    answer = 0
    temp = []
    while len(score) > 0:
        temp.append(max(score))
        score.pop(score.index(max(score)))
        if len(temp) == m:
            answer = answer + min(temp) * m
            temp = []
    return answer