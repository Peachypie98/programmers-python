def solution(N, stages):
    answer = []
    accumulated = 0
    for i in range(1, N+1):
        if(stages.count(i) == 0):
            answer.append((0, i))
        else:
            answer.append((stages.count(i) / (len(stages) - accumulated),i))
            accumulated += stages.count(i)
    answer.sort(key = sort, reverse = True)
    return [a[1] for a in answer]
    
def sort(e):
    return e[0]