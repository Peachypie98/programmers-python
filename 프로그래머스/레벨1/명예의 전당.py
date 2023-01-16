def solution(k, score):
    a = []
    answer = []
    for i in score:
        if (len(a) < k):
            a.append(i)
            a.sort()
            answer.append(a[0])
            continue
        else:
            for idx, y in enumerate(a):
                if (i > y):
                    a[idx] = i
                    a.sort()
                    answer.append(a[0])
                    break
                else: 
                    answer.append(a[0])
                    break
    return answer