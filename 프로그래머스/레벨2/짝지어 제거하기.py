from collections import deque
def solution(s):
    char = deque()
    for i in s:
        char.append(i)
        if(len(char) == 1):
            continue
        elif(char[len(char)-1] == char[len(char)-2]):
            char.pop()
            char.pop()
    if len(char) == 0: return 1
    else: return 0