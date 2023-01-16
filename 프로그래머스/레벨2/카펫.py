def solution(brown, yellow, answer = 0):
    row = 2
    column = 3
    while(True):
        row += 1
        if((row-2) * (column-2) == yellow and (row*column) - yellow == brown):
            return [row, column]
        m = column
        while(m != row):
            m += 1
            if((row-2) * (m-2) == yellow and (row*m) - yellow == brown):
                return [row, m]  