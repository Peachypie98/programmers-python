def solution(mylist):
    total = []
    for operation in mylist:
        if operation[:1] == "I":
            total.append(int(operation[2:]))
        if operation[:3] == "D -" and total:
            total.remove(min(total))
        if operation[:3] == "D 1" and total:
            total.remove(max(total))
    if total:
        answer = [max(total), min(total)]
    else:
        answer = [0, 0]
    return answer