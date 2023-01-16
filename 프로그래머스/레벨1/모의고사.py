def solution(answers):
    one = [1,2,3,4,5]*10000
    two = [2,1,2,3,2,4,2,5]*10000
    three = [3,3,1,1,2,2,4,4,5,5]*10000
    
    count1 = 0
    count2 = 0
    count3 = 0
    for idx, i in enumerate(answers):
        if(i == one[idx]):
            count1 += 1
        if(i == two[idx]):
            count2 += 1
        if(i == three[idx]):
            count3 += 1
    
    answer = []
    for idx, x in enumerate([count1,count2,count3], start=1):
        if(x == max([count1,count2,count3])):
            answer.append(idx)
    return answer