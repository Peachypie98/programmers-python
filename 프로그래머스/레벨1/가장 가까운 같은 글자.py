def solution(s):
    answer = []
    for i in range(len(s)):
        j = i-1
        while True:
            if j == -1:
                answer.append(-1)
                break
            elif s[i] == s[j]:
                answer.append(i-j)
                break
            else:
                j = j-1
    return answer