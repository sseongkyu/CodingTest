n = int(input())
crd = list(map(int, input().split(' ')))

new_crd = sorted(list(set(crd)))
crd_dic = {new_crd[i]: i for i in range(len(new_crd))}
for i in crd:
    print(crd_dic[i], end=' ')
