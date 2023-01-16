def solution(a, b, n):
    count = 0
    while(n >= a):
        quo, remain = divmod(n,a)
        count += quo*b
        n = quo*b+remain 
    return count