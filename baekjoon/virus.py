com = int(input())
edge = int(input())

visited = [False]*(com+1)
graph = [[] for _ in range(com+1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()


def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = True


dfs(1)
print(visited.count(True)-1)
