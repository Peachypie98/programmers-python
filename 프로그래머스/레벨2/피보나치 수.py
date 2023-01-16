def solution(n):
    count = 1
    a = 0
    b = 1
    while(count != n):
        x = a + b
        a = b
        b = x
        count +=1
    return x % 1234567