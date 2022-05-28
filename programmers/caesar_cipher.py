# 내 코드

def solution(s, n):
    answer = ''
    for i in s:
        d = ord(i)
        for _ in range(n):
            if d == 122:
                d = 96
            elif d == 90:
                d = 64
            elif d == 32:
                d = 31
            d += 1
        answer += chr(d)
    return answer

# 다른사람 코드


def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A') + n) % 26+ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a') + n) % 26+ord('a'))
            # 주어진 문자와 A,a(시작하는 문자)의 차이에서 옆으로 옮길 수 n을 더한값에 % 연산으로 통해 A~Z, a~z사이에서 얼만큼 움직였는지 알수있음
    return "".join(s)
