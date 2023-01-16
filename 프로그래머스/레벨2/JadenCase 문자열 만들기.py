def solution(s):
    s = s.title() 
    str1 = ""
    digit = False
    space = False
    
    for char in s:
        if(char.isdigit()):
            str1 += char
            digit = True
            space = False
        elif(digit == True):
            str1 += char.lower()
            digit = False
        elif(char == " "):
            str1 += char
            space = True
        elif(space == True):
            str1 += char.upper()
            space = False
        else:
            str1 += char
    return str1
    