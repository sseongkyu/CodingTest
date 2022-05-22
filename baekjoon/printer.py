from collections import deque


def solution(priorities, location):
    answer = 0

    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        printout = d.popleft()
        print(d)
        if d and max(d)[0] > printout[0]:
            d.append(printout)
        else:
            answer += 1
            if printout[1] == location:
                break

    return print(answer)


solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)
