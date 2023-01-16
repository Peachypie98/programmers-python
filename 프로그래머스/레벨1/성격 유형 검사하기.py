def solution(survey, choices):
    table = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in zip(survey, choices):
        point = point_converter(i[1])
        if(point == 0):
            continue
        elif(i[1] > 4):
            char = i[0][1]
            table[char] += point
        else:
            char = i[0][0]
            table[char] += point
            
    answer = ''
    answer += 'R' if (table['R'] >= table['T']) else 'T'
    answer += 'C' if (table['C'] >= table['F']) else 'F'
    answer += 'J' if (table['J'] >= table['M']) else 'M'
    answer += 'A' if (table['A'] >= table['N']) else 'N'
    return answer
         
def point_converter(x):
    if   (x == 1 or x == 7): return 3
    elif (x == 2 or x == 6): return 2
    elif (x == 3 or x == 5): return 1
    else : return 0