import math
def solution(n, k):
    # convert to base k
    num = str(convert(n,k))
    
    # find all prime numbers 
    final = []
    for i in num.split("0"):
        if(i == "" or i == "1"):
            continue
        elif(isprime(int(i))):
            final.append(i)
            
    # check how many conditions are met for each prime number  
    count = 0
    for i in final:
        length = len(i)
        if("0"+i+"0" in num):
            count += 1
        elif(i+"0" in num):
            count += 1
        elif("0"+i in num):
            count += 1
        elif(i in num):
            count += 1
    return count

def convert(n, k):
    string = ""
    quotient = n
    while(quotient != 0):
        quotient, remainder = divmod(quotient,k)
        string += str(remainder)
    return int(string[::-1])

def isprime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if(x % i == 0):
            return False
    return True