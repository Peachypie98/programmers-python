def solution(s, skip, index):
    book = {"a":1, "b":2, "c": 3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
            "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
            "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
    book_reversed = {v:k for k,v in book.items()}
    tmp = []
    answer = []
    for i in s:
        num = book.get(i) 
        num2 = num + index
        for x in range(num+1,num2+1):
            if(x > 26):
                x -= 26
            tmp.append(book_reversed.get(x))
        while(check(tmp, skip) != False):
            for char in skip:
                if(char in tmp):
                    tmp.remove(char)
            while(len(tmp) != index):
                num2 += 1
                if(num2 > 26):
                    num2 -= 26
                tmp.append(book_reversed.get(num2))
        answer.append(tmp[index-1])
        tmp.clear()         
    return "".join(answer)

def check(tmp, skip):
    for char in skip:
        if(char in tmp):
            return True
    return False

print(solution("adqzzy", "yd", 1))