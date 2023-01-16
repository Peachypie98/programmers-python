def solution(strings, n):
    char_list = []
    answer = []
    for i in strings:
        char_list.append(i)
    char_list.sort()
    for i in char_list:
        answer.append(i)
    return answer