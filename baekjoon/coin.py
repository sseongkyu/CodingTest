n, k = map(int, input().split(' '))
coin = []
count = 0

for _ in range(n):
    coin.append(int(input()))
coin.reverse()
for i in range(n):
    if coin[i] > k:
        continue
    if k != 0:
        count += k // coin[i]
        k %= coin[i]
        if k == 0:
            print(count)
            break
