ch = list(input().upper())
set_ch = list(set(ch))
result = []
idx_ch = {}

for i, j in enumerate(set_ch):
    idx_ch[ch.count(j)] = i
    result.append(ch.count(j))
m = max(result)

if result.count(m) >= 2:
    print('?')
else:
    print(set_ch[idx_ch[m]])
