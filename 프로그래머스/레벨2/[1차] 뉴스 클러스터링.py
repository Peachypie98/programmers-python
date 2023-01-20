import itertools as it
def solution(str1, str2):
    # data processing 1
    str1 = str1.lower()
    str2 = str2.lower()
    
    # pairwise
    set1 = list()
    set2 = list()
    for i in pairwise(str1):
        set1.extend({i[0]+i[1]})
            
    for j in pairwise(str2):
        set2.extend({j[0]+j[1]})
    
    # data processing 2
    set1 = [i for i in set1 if i.isalpha()]
    set2 = [i for i in set2 if i.isalpha()]
    
    # intersection
    intersection = []
    tmp = set2.copy()
    for i in set1:
        if(i in tmp):
            tmp.remove(i)
            intersection.append(i)
            
    # union
    union = len(set1) + len(set2) - len(intersection)

    # multiplication
    if (len(set1) == 0 and len(set2) == 0):
        multiplier = 1
    else:
        multiplier = len(intersection)/union
    return int(65536*multiplier)

def pairwise(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)

print(solution("abab", "baba"))