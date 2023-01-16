def solution(n, lost, reserve):
    # 1단계
    l = set()
    r = set()
    for i in reserve:
        r.add(i)
    for x in lost:
        l.add(x)
    c = l.intersection(r)
    
    # 2 단계
    reserve = reserve.copy()
    lost = lost.copy()
    if(len(c) > 0):
        for i in c:
            reserve.remove(i)
            lost.remove(i)
    
    # 3단계
    reserve.sort()
    lost.sort() 
    for i in lost:
        if(i-1 in reserve):
            reserve.remove(i-1)
            continue
        if(i in reserve):
            reserve.remove(i)
            n -=1
            continue
        if(i+1 in reserve):
            reserve.remove(i+1)
            continue
        n -= 1
    return n