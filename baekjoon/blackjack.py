n, m = map(int, input().split(' '))
card = list(map(int, input().split(' ')))
sum_list = []
new_list = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum_list.append(int(card[i])+int(card[j])+int(card[k]))

for value in sum_list:
    if value <= m:
        new_list.append(value)
print(max(new_list))
