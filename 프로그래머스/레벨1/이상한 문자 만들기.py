def solution(s):
    s = s.split(" ")
    tmp2 = []
    for word in s:
        tmp = ""
        for idx, x in enumerate(word, start =1):
            if(idx % 2 != 0):
                tmp += x.upper()
            else:
                tmp += x.lower()
        tmp2.append(tmp)           
    return " ".join(tmp2)