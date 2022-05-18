from collections import deque

n = int(input())
card = deque([i for i in range(1, n+1)])

while len(card) > 1:
    card.popleft()
    ch_num = card.popleft()
    card.append(ch_num)
print(card[0])
