import math
def solution(n):
    count = 0
    for i in range(2,n+1):
        if(is_prime(i)):
            count += 1
    return count

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    return True