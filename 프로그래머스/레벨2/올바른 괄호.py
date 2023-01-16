def solution(s):
    # 효율성
    if(s.startswith(")")):
        return False
    elif(s.count("(") != s.count(")")):
        return False
    # 찐 코드
    else:
        count = 0
        for i in s:
            if(i == "("):
                count += 1
            elif(i == ")" and count != 0):
                count -= 1
            else:
                return False
        return True
            
        