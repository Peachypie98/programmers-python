from collections import Counter
def solution(clothes):
    clothes_list = []
    for i in clothes: 
        clothes_list.append(i[1])
    a = Counter(clothes_list)
    c = 1
    for i in a.values():
        c *= i+1
    return c - 1