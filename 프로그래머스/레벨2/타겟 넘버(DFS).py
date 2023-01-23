def solution(numbers, target):
    count = 0
    stack = [(0,0)]
    while stack: 
        stage, value = stack.pop()
        if stage == len(numbers):
            if(value == target):
                count += 1
            continue
        stack.append((stage+1, value+numbers[stage]))
        stack.append((stage+1, value-numbers[stage]))
    return count