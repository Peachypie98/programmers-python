def solution(t, p):
    extracted_number = []
    answer = 0 
    while(len(t) >= len(p)):
        extracted_number.append(t[:len(p)])
        t = t[1:]

    answer = answer + 1 for x in extracted_number if (int(x) < int(p))   
    return answer