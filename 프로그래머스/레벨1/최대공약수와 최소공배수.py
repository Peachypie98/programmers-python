def solution(n, m):
    lowest = n if n < m else m
    GCF = 0
    LCM = 0
    answer = []
    
    # 최대공약수
    for i in range(1,lowest+1):
        if(n % i == 0 and m % i == 0):
            GCF = i
    
    # 최소공배수
    a = n if n > m else m
    i = 2
    while(i <= a):
        if (n % i != 0 or m % i != 0): # n remainder is not 0, m remainder is not 0
            i += 1
            continue
        n = n // i
        m = m // i
        a = n if n > m else m
    LCM = GCF * n * m
    answer.extend([GCF, LCM])
    return answer