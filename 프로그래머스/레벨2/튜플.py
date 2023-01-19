def solution(s):
    s = s[1:]
    s = s[:len(s)-1]
    answer = []
    final = []
    while(len(s) != 0):
        left = s.find("{")
        right = s.find("}")
        answer.append(s[left:right+1])
        s = s[right+1:]
    answer.sort(key = sort)
    
    for i in answer:
        i = i.replace("{", "")
        i = i.replace("}", "") # i = 111, 20, 111
        if("," not in i):
            if(int(i) not in final):
                final.append(int(i))
        else:
            for x in i.split(","):
                if(int(x) not in final):
                    final.append(int(x))         
    return final

def sort(e):
     return len(e)