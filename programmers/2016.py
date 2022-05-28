# 내 코드
import datetime


def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = datetime.date(2016, a, b)

    return days[day.weekday()]

# datetime 모듈의 date() 메소드 사용
# 0 : 월 1 : 화 ~~~ 5 : 토 6 : 일
