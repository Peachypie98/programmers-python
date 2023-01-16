def solution(food):
    del food[0]
    answer = ""
    for idx, i in enumerate(food, start = 1):
        divide = i//2
        answer += str(idx) * divide    
    return answer + "0" + answer[::-1]