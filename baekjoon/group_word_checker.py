total = 0
n = int(input())
for _ in range(n):
    result = 0
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new = word[i+1:]
            if new.count(word[i]) > 0:
                result += 1
    if result == 0:
        total += 1
print(total)
