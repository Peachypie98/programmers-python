import itertools as it
def solution(d, budget):
    # special case:
    if (sum(d) == budget):
        return len(d)
    elif (sum(d) < budget):
        return len(d)
     
    d = sorted(d)
    acc = 0
    for idx, i in enumerate(d, start = 1):
        acc += i
        if(acc > budget):
            return idx-1
        elif(acc == budget):
            return idx