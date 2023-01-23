import math
from itertools import permutations
def solution(numbers):
    count = 0
    stack = []
    for x in range(1, len(numbers)+1):
        for i in permutations(numbers, x):
            num = "".join(i)
            if(num.startswith("0") and len(num) != 1):
                num = num.replace("0", "",1)
            if(isprime(int(num)) == True and int(num) not in stack):
                count += 1
                stack.append(int(num))
    return count


def isprime(x):
    if(x == 1 or x == 0):
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    return True
