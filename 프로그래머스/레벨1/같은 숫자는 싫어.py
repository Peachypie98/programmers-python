def solution(arr):
    answer = []
    for i in arr:
        if(len(answer) < 1):
            answer.append(i)
        elif(answer[len(answer)-1] != i):
            answer.append(i)
    return answer