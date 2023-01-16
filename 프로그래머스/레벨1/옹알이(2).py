def solution(babbling, answer = 0):
    for i in babbling:
        if (i.count("yeye") >= 1 or i.count("ayaaya") >= 1 or i.count("mama") >= 1 or i.count("woowoo") >=1):
            continue
        else: 
            while(len(i) != 0):
                if i.startswith("aya"):
                    i = i[3:]
                elif (i.startswith("ye")):
                    i = i[2:]
                elif (i.startswith("ma")):
                    i = i[2:]
                elif (i.startswith("woo")):
                    i = i[3:]
                else:
                    answer -= 1
                    break
            answer +=1
            
    return answer