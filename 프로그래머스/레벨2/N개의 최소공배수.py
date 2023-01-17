# LCM(a,b,c,d) = LCM(LCM(LCM(a,b),c),d)
# LCM(a,b,c) = LCM(LCM(a,b),c)
# LCM(a,b) = a*b / GCD(a,b)
import math
def solution(myArr):
    if (len(myArr) == 1):
        return myArr[0]
    elif (len(myArr) == 2):
        return lcm(myArr[0], myArr[1])
    else:
        tmp = lcm(myArr[0], myArr[1])
        myArr.pop(0)
        myArr.pop(0)
        for i in myArr:
            tmp = lcm(tmp, i)
        return tmp
def lcm(a, b):
    return int((a * b) / math.gcd(a, b))