def solution(n):
    answer = 0
    for idx, i in enumerate(base3(n)):
        answer += int(i) * pow(3, idx)
    return answer

def base3(x):
    quo = x
    base = ""
    while(quo != 0):
        A = divmod(quo,3)
        quo = A[0]
        base += str(A[1])
    return base[::-1]