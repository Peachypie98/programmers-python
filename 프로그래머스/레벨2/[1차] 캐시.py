def solution(cacheSize, cities):
    cache = []
    time = 0
    if (cacheSize == 0):
        for i in cities:
            time += 5
        return time
        
    for i in cities:
        if(i.lower() not in cache):
            time += 5
        else:
            time +=1
            tmp = cache[cache.index(i.lower())] # S
            del cache[cache.index(i.lower())]
            cache.append(tmp)
            continue
            
        if (len(cache) != cacheSize):
            cache.append(i.lower())
        else:
            del cache[0]
            cache.append(i.lower())
            
    answer = time
    return answer