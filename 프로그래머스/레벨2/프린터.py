from collections import deque
def solution(priorities, location):
    target_num = priorities[location]
    max_num = max(priorities)
    priorities = deque(priorities)
    answer = []
    location = location + 1
    while(True):
        while(priorities[0] != max_num):
            priorities.rotate(-1)
            if (location == 1):
                location = len(priorities)
            else:
                location -= 1      
        
        if(location == 1 and max(priorities) == target_num):
            return len(answer)+1
        else:  
            digit = priorities.popleft()
            answer.append(digit)
            max_num = max(priorities)
            location -= 1