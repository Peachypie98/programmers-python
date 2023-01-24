def solution(phone_number):
    last_four = phone_number[len(phone_number)-4:]
    return "*"*(len(phone_number)-4) + last_four