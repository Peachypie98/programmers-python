def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for idx, i in enumerate(phone_book):
        if(idx+1 >= length):
            break
        if(i == phone_book[idx+1][:len(i)]):
            return False
    return True