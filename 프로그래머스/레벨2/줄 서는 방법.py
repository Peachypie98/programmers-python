import math
def solution(n, k):
    num = [i for i in range(1,n+1)]
    answer = []
   
    while(len(num) != 0):
        n = len(num)
        total_combinations = math.factorial(n) # 3! = 6
        digit_change = int(total_combinations / n) # 6/3 = 2
        digit = math.ceil(k/digit_change) - 1
        answer.append(num[digit])
        num.remove(num[digit])
        
        tmp = k
        while(tmp >= math.factorial(n-1)):
            tmp -= math.factorial(n-1)
        k = tmp
    return answer