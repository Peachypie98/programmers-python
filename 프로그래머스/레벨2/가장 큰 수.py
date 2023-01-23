import itertools as it
def solution(numbers):
    if(numbers.count(0) == len(numbers)):
        return str(0)
    
    numbers = [str(i) for i in numbers]
    for idx, i in enumerate(numbers):
        numbers[idx] = (numbers[idx] * 4, i)
    numbers.sort(reverse = True)
    
    for idx, i in enumerate(numbers):
        numbers[idx] = numbers[idx][1]
    return "".join(numbers)  