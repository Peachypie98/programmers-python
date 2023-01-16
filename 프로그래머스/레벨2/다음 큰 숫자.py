def solution(n):
    old = two_bit_converter(n)
    while(True):
        n += 1
        new = two_bit_converter(n)
        if(old.count("1") == new.count("1")):
            return n
     
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