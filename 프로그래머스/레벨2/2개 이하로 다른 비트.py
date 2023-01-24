def solution(numbers):
    answer = []
    for i in numbers:
        if(i % 2 == 0):
            answer.append(i+1)
        else:
            real = bin(i)[2:]
            print(real)
            if(real.endswith("0")):
                real = str(int(real) + 1)
                answer.append(convert(real))
            elif(real.find("0") == -1):
                real = real.zfill(len(real)+1)
                real = [i for i in real]
                real[0] =  "1"
                real[1] = "0"      
                answer.append(convert("".join(real)))
            else:
                location = real.rfind("0")
                real = [i for i in real]
                real[location+1] = "0"
                real[location] = "1"
                answer.append(convert("".join(real)))
    return answer

def convert(x):
    x = x[::-1]
    value = 0
    for idx, i in enumerate(x):
        value += int(i) * (2**idx)
    return value             