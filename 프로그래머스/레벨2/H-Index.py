def solution(citations):
    citations.sort(reverse=True)
    thesis = [i for i in range(1,len(citations)+1)]
    for idx, i in enumerate(thesis):
        if(i > citations[idx]):
            return i-1
    return len(thesis)