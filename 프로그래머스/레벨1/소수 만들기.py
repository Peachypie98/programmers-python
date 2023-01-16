import itertools as it
def solution(nums):
    count = 0
    for i in it.combinations(nums, 3):
        if(is_prime(sum(i)) == True):
            count += 1
    return count
         
def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True