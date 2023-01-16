import math
def solution(number, limit, power, count =0):
    list1 = list()
    for i in range(1, number+1):
        for x in range(1, int(math.sqrt(i)) + 1):
            if(i % x == 0):
                if (i // x == x):
                    count +=1         
                else: 
                    count += 2  
        list1.append(count)
        count = 0
    return sum([x if x <= limit else power for x in list1])