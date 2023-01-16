from collections import Counter

def solution(nums):
    take = len(nums)/2
    species = Counter(nums)
    count = 0
    for i in species:
        count += 1
    if (count < take): answer = count
    elif (count == take): answer = count
    else: answer = take
    return answer