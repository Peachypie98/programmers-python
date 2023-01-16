def solution(s):
    answer = s.split()
    answer = [int(x) for x in answer]
    lowest = min(answer)
    biggest = max(answer)
    answer = f"{lowest} {biggest}"
    return answer