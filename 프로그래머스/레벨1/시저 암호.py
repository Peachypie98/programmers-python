def solution(s, n):
    char_dict = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 
                 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 
                 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
    char_dict_reversed = {v:k for k,v in char_dict.items()}
    
    answer = ""
    for i in s:
        if(i == " "):
            answer += " "
            continue
        elif(i.isupper()):
            old = char_dict_reversed.get(i.lower())
            new = old+n
            if(new > 26):
                new -= 26
            answer += char_dict.get(new).upper()
        else:
            old = char_dict_reversed.get(i.lower())
            new = old+n
            if(new > 26):
                new -= 26
            answer += char_dict.get(new)
    return answer