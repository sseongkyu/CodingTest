commands = [[1, 2, 4], [5, 3, 2]]
for i in range(len(commands[:])):
    for i, j, k in zip(str(commands[i][0], commands[i][1], commands[i][2])):
        print(i, j, k)
