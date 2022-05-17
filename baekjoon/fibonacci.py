n = int(input())

fibo_list = [0, 1]
if n == 0 or n == 1:
    if n == 0:
        print(fibo_list[0])
    else:
        print(fibo_list[1])
else:
    for i in range(2, n+1):
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
    print(fibo_list[n])
