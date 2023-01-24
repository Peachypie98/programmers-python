def solution(x, n):
    # special case
    if x == 0:
        return [0]*n
    
    answer = []
    if x > 0:
        for i in range(x,n*x+1,x):
            answer.append(i)
    else:
        x = x*-1
        for i in range(x, n*x+1, x):
            answer.append(i)
        for idx, i in enumerate(answer):
            answer[idx] = answer[idx]*-1        
    return answer