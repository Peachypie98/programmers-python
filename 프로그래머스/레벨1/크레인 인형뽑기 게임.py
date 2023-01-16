def solution(board, moves):
    bucket = []
    answer = 0
    for move in moves: # move = 1,5,3,5...
        for i in board: # i = [0,0,0,0,0], [0,0,1,0,3], ...
            if(i[move-1] != 0):
                bucket.append(i[move-1])
                i[move-1] = 0
                break
        if(len(bucket) != 1):
            for idx, i in enumerate(bucket):
                if (idx == len(bucket)-1):
                    break
                elif (bucket[idx] == bucket[idx+1]):
                    bucket.pop(idx)
                    bucket.pop(idx)
                    answer += 2
                    break
    return answer