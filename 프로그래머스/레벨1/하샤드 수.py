def solution(x):
    value = 0
    for i in str(x):
        value += int(i)
    if(x % value == 0):
        return True
    return False