def solution(s):
    zero_count = 0
    loop_count = 0
    while(s != "1"):
        loop_count += 1
        zero_count += s.count("0")
        for i in range(s.count("0")):
            s = s.replace("0", "")
        s = two_bit_converter(len(s))
    
    answer = [loop_count, zero_count]
    return answer

def two_bit_converter(x):
    list1 = []
    quotient = x
    while (quotient != 0):
        remainder = quotient % 2
        quotient = quotient // 2
        list1.append(str(remainder))
    list1 = list1[::-1]
    bit = "".join(list1)
    return bit
    