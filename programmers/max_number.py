# 내 코드

def solution(numbers):
    answer = ''
    number = list(map(str, numbers))
    number = sorted(number, key=lambda x: (
        x[0], x[1 % len(x)], x[2 % len(x)], x[3 % len(x)]), reverse=True)
    answer = ''.join(number)
    return answer if int(answer) != 0 else '0'

# 다른사람코드


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
