def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if(divisor(i) % 2 == 0):
            answer +=i
        else:
            answer -= i
    return answer

def divisor(x):
    tmp = []
    for i in range(1, x+1):
        if(x % i == 0):
            tmp.append(i)
    return len(tmp)