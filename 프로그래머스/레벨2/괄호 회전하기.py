from collections import deque
def solution(s):
    stack = deque(s)
    stack2 = deque()
    count = 0
    open_ = {"[":"]", "(":")", "{":"}"}
    closed_ = {']':'[', ')':'(', '}':'{'}
    for i in range(len(s)):
        check = False
        for y in stack:
            if(len(stack2) == 0 and y in closed_):
                check = True
                break
            elif(y in open_):
                stack2.append(y)
            elif(y in closed_ and stack2[-1] == closed_.get(y)):
                stack2.pop()
            else:
                check = True
                break
        if(len(stack2) == 0 and check != True):
            count += 1
        stack.rotate(-1)
    return count