def solution(storey):
    answer = 0
    storey_norm = str(storey)
    if int(storey_norm[0]) > 5:
        answer += 1
        storey = str(10**len(storey_norm) - storey)[::-1]
    elif int(storey_norm[0]) == 5 and int(storey_norm[1]) >= 5:
        answer += 1
        storey = str(10**len(storey_norm) - storey)[::-1]
    else:
        storey = str(storey)[::-1]
    add = False
    for i in range(len(storey)):
        num = int(storey[i])
        if add:
            num += 1
        if num <= 5:
            answer += num
            add = False
        else:
            answer += 10 - num
            add = True
    return answer