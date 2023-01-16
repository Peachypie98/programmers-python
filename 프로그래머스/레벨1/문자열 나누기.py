def solution(s, count=0, count1=0, answer=0):
    char = None
    for idx, i in enumerate(s):
        if (idx == len(s)-1): answer +=1    
        elif (char == None):
            char = i
            count += 1    
        elif (i == char): count += 1   
        else:
            count1 += 1
            if (count == count1):
                answer +=1
                count = 0
                count1 = 0
                char = None
    return answer