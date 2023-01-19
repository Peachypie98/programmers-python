import numpy as np
def solution(n, left, right):
    answer = []
    row_l = 1
    row_r = 1
    count = right - left
    if(left > n):
        while(left > n):
            left -= n
            row_l += 1
            
    if(right > n):
        while(right > n):
            right -= n
            row_r += 1  
            
    row = row_l        
    for i in range(row,n+1):
        for j in range(1,n+1):
            if(row <= j):
                answer.append(j)    
            else:
                answer.append(row)
        if(row == row_r):
            break
        row+=1
    return answer[left:left+count+1]