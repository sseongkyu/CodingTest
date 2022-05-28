# 내 코드
import math


def solution(progresses, speeds):

    answer = []
    f = []
    for i, j in zip(progresses, speeds):
        f.append(math.ceil((100-i)/j))
    for idx in range(1, len(f)):
        if f[idx] < f[idx-1]:
            f[idx] = f[idx-1]
    set_f = sorted(set(f))
    for i in range(len(set_f)):
        answer.append(f.count(set_f[i]))
    return answer

# 다른사람코드


def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):  # 올림을 쓰지 않기 위해 -((p-100)//s) 사용
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]
