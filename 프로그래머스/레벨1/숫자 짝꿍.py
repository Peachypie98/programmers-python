from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    final = dict()
    a = []
    for i in x.items(): 
        value = y.get(i[0],-1)
        if(i[1] > value):
            final[i[0]] = value
        else:
            final[i[0]] = i[1]

    for i in final.items():
        for x in range(i[1]):
            a.append(int(i[0]))
    a.sort(reverse=True)
    
    print(final)
    print(a)

    if(len(a) == 0):
        return "-1"
    else:
        if (a.count(0) == len(a)):
            a = [a[0]]
        answer = [str(i) for i in a]
        answer = "".join(answer)
    return answer