def solution(n):
    count = 1 
    for i in range(1, n): # 1-14
        count += modified_factorial(i, n) 
    return count

def modified_factorial(x, limit):
    sum = x
    for i in range(x+1,limit+2): # 2-14
        sum += i
        if(sum > limit):
            return 0
        elif(sum == limit):
            return 1