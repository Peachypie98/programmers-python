def solution(dartResult):
    types = {"S":1, "D": 2, "T":3}
    A = [i for i in dartResult]
    answer = []
    while(len(A) != 0):
        try:
            if(A[2] == "*"):
                if(dartResult[-1] == "*" and dartResult[2] != "*"):
                    answer[len(answer)-1] *= 2 
                    answer.append(pow(int(A[0]),types.get(A[1])) * 2)
                    A.pop(0)
                    A.pop(0)
                    A.pop(0)
                else:  
                    if(len(answer) == 0):
                        answer.append(pow(int(A[0]),types.get(A[1]))*2)
                        A.pop(0)
                        A.pop(0)
                        A.pop(0)
                    else:
                        answer[len(answer)-1] *= 2 
                        answer.append(pow(int(A[0]),types.get(A[1])) * 2)
                        A.pop(0)
                        A.pop(0)
                        A.pop(0)
            elif(A[2] == "#"):
                answer.append(pow(int(A[0]),types.get(A[1])) * -1)
                A.pop(0)
                A.pop(0)
                A.pop(0)
            elif(A[2].isalpha()):
                answer.append(pow(10,types.get(A[2])))
                A.pop(0)
                A.pop(0)
                A.pop(0)
            else:
                answer.append(pow(int(A[0]),types.get(A[1])))
                A.pop(0)
                A.pop(0)
        except:
            answer.append(pow(int(A[0]),types.get(A[1])))
            A.pop(0)
            A.pop(0)
    return sum(answer)
print(solution("1S*2T#3S"))