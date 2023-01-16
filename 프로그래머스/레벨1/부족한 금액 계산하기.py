def solution(price, money, count):
    total_price = 0
    a = price
    for i in range(count):
        total_price += price
        price += a
    if (money < total_price):
        return total_price - money
    else: return 0