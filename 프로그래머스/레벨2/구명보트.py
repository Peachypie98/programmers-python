from collections import deque
def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    count = 0
    while(len(people) != 0):
        if(len(people) == 1):
            count +=1
            break
        if(people[0] + people[-1] <= limit):
            count += 1
            people.pop()
            people.popleft()
        else:
            count +=1
            people.popleft()
    return count