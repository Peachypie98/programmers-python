from collections import deque
def solution(ingredient):
    ingredient = deque(ingredient)
    copy1 = deque()
    count = 0
    for i in ingredient:
        copy1.append(i)
        if(len(copy1) == 3):
            continue
        elif(copy1[len(copy1)-1] == 1 and copy1[len(copy1)-2] == 3 and copy1[len(copy1)-3] == 2 and copy1[len(copy1)-4] == 1):
            copy1.pop()
            copy1.pop()
            copy1.pop()
            copy1.pop()
            count +=1
    return count