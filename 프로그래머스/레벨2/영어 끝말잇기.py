def solution(n, words):
    words_said = []
    last_char  = words[0][::-1][0]
    words_said.append(words[0])
    tmp = False
    check = False
    person = 0
    count = 1
    count1 = 0
    for idx, i in enumerate(words, start=1):
        if tmp == False:
            tmp = True
            continue
            
        first_char = i[0] 
        count1 += 1
        if (count1 == n):
            count +=1
            count1 = 0
            
        if (last_char != first_char):
            if(idx <= n):
                person = idx
                check = True
                break
            else:
                while(idx > n):
                    idx = idx-n
                person = idx
                check = True
                break
        elif (i in words_said):
            if (idx <= 3):
                person = idx
                check = True
                break
            else:
                while(idx > n):
                    idx = idx-n
                person = idx
                check = True
                break
        last_char = i[::-1][0]
        words_said.append(i)
    
    if (check == False):
        return [0,0]
    else:
        return [person, count]