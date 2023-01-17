def solution(n):
    # special case
    if(n == 1):
        return 1
    
    memory = [0 for i in range(n+1)]
    memory[0] = 0
    memory[1] = 1
    for i in range(2, n+1):
        memory[i] = memory[i-1] + memory[i-2] 
    return (memory[-1] + memory[-2]) % 1234567
