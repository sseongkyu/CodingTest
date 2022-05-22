# 내 코드

def solution(people, limit):
    answer = 0
    start = 0
    end = len(people)-1
    people.sort(reverse=True)
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            end -= 1
        start += 1
    return answer
