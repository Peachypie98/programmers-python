from collections import deque
def solution(progresses, speeds):
    prog = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while(len(prog) != 0):
        count = 0
        for idx, i in enumerate(prog):
            prog[idx] += speeds[idx]
        for idx, i in enumerate(prog):
            if(prog[idx] >= 100):
                count +=1
            else:
                break   
        for i in range(count):
            prog.popleft()
            speeds.popleft()
        if(count != 0):
            answer.append(count)
    return answer