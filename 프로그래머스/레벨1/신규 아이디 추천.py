def solution(new_id):
    # 1 단계
    new = new_id.lower()
    
    # 2 단계
    for i in new:
        if not(i == "-" or i == "_" or i == "." or i.isalnum()):
            new = new.replace(i, "")
    
    # 3 단계
    check = False
    str1 = ""
    for idx, i in enumerate(new):
        if (check == False and i == "."):
            str1 += i
            check = True
        elif (i != "."):
            str1 += i
            check = False
    new = str1
            
    # 4 단계
    if(new.startswith(".")):
        new = new[1:]
    elif (new.endswith(".")):
        new = new[:len(new)-1]
    
    # 5 단계
    if (new == ""):
        new = "a"
        
    # 6 단계
    if (len(new) >= 16):
        new = new[:15]
    if (new.endswith(".")):
        new = new[:len(new)-1]
        
    # 7 단계
    if (len(new) <= 2):
        take_char = new[len(new)-1]
        while(len(new) < 3):
            new += take_char
    
    return new