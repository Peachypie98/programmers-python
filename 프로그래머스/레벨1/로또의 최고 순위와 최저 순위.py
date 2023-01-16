def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    A = set()
    B = set()
    for i in range(6):
        A.add(lottos[i])
        B.add(win_nums[i])
    C = A.intersection(B)
    return [rank.get(len(C)+lottos.count(0)),rank.get(len(C))]