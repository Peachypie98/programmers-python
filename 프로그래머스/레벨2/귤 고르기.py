from collections import Counter
def solution(k, tangerine):
    tangerine.sort()
    tangerine = Counter(tangerine)
    tmp = []
    for i in tangerine.items():
        tmp.extend([i])
    tmp.sort(reverse = True, key = lambda x: x[1])
    
    tmp2 = []
    for i in tmp:
        if(k <= 0):
            break
        k -= i[1]
        tmp2.append(i)
    return len(tmp2)