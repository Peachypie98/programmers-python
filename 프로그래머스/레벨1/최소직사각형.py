def solution(sizes):
    height = [min(i) for i in sizes]
    width  = [max(i) for i in sizes]
    return max(height) * max(width)