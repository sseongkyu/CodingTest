from collections import deque


def bfs(p):
    p_idx = []
    # P값이 있는 자리를 i,j 인덱스로 저장
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                p_idx.append([i, j])

    for s in p_idx:
        queue = deque([s])
        visited = [[0]*5 for i in range(5)]  # 방문처리 초기화
        distance = [[0]*5 for i in range(5)]  # 경로 길이 초기화
        visited[s[0]][s[1]] = 1  # 초기 P값을 방문처리

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []
    for i in places:
        answer.append(bfs(i))
    return answer
