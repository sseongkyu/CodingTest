# 파이썬에서 수열을 출력하는 문제
import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m)

for i in array:
    for j in i:
        print(j, end=' ')
    print()

# 백트래킹 활용!! 개념학습하고 다시 풀기

n, m = map(int, input().split())
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
