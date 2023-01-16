from collections import Counter
def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    for i in a:
        if(b.get(i) != a.get(i)):
            return i 