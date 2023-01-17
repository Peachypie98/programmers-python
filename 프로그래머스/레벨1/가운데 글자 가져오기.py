def solution(s):
    if (len(s) % 2 == 0): # even
        return s[int((len(s)/2)-1):int((len(s)/2)+1)]
    return s[int(len(s)/2)]
        