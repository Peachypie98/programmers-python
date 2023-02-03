def solution(genres, plays):
    combined = []
    final = dict()
    answer = []
    for idx, i in enumerate(genres):
        combined.append((i,plays[idx]))
    
    for idx, i in enumerate(combined):
        if(i[0] not in final):
            final[i[0]] = i[1]
        else:
            final[i[0]] = final.get(i[0]) + i[1]
            
    check = []
    for i in final.items():
        check.append(i)
    check.sort(key = lambda x: x[1], reverse = True)
    
    for i in check:
        count = 0
        while(count != 2):
            check = False
            genre = i[0] 
            tmp = 0
            tmp_idx = 0
            for idx, x in enumerate(combined):
                if(x[0] == genre and tmp < x[1]):
                    tmp = x[1]
                    tmp_idx = idx
                    check = True
            if(check == True):
                answer.append(tmp_idx)
                combined[tmp_idx] = (genre,0)
                count += 1
            else:
                count +=1
                continue
    return answer
