n = int(input())
bulk_list = [0]*n
result = []
for i in range(n):
    bulk_list[i] = list(map(int, input().split(' ')))

for i in range(n):
    bulk = 1
    for j in range(n):
        print(i, bulk_list[i][0] < bulk_list[j][0]
              and bulk_list[i][1] < bulk_list[j][1])
        print(i, bulk_list[i][0], bulk_list[j][0],
              bulk_list[i][1], bulk_list[j][1])
        if bulk_list[i][0] < bulk_list[j][0] and bulk_list[i][1] < bulk_list[j][1]:
            bulk += 1
    result.append(bulk)
print(result)
