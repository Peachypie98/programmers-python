def solution(a, b):
    mon = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    idx = 0
    answer = ""
    for c,i in enumerate(mon, start=1):
        for y in range(1, i+1): 
            if (c== a and y == b):
                return date[idx]
            else:
                if (idx == 6):
                    idx = 0
                else:
                    idx +=1
        
    return answer