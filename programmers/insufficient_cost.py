# 내 코드
def solution(price, money, count):
    total_price = 0
    answer = -1
    for i in range(1, count+1):
        total_price += price*i
    if money - total_price < 0:
        return total_price - money
    else:
        return 0

# 다른사람 코드


def solution(price, money, count):
    return abs(min(money-sum([price*i for i in range(1, count+1)]), 0))
