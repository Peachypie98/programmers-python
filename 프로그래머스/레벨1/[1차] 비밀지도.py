def solution(n, arr1, arr2):
    c = [n] * n
    arr1 = list(map(two_bit, c, arr1))
    arr2 = list(map(two_bit, c, arr2))
    answer = ""
    a = []
    for x,y in zip(arr1, arr2):
        for i in range(n):
            if(x[i] == y[i] and x[i] == "0"):
                answer += " "
            else:
                answer += "#"
        a.append(answer)
        answer = ""
    return a;

def two_bit(n, num):
    bit = ""
    while(num != 0):
        quotient = num // 2
        bit += str(num % 2)
        num = quotient
    bit = bit[::-1]
    if (n > len(bit)):
        bit = "0"*(n-len(bit)) + bit
    return bit