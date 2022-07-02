from collections import deque
n, m = map(int, input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1이 괴물 없는 곳
def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        result = 0
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 범위를 벗어나는 경우
                continue
            if graph[nx][ny] == 0:  # 괴물이 있는 경우
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    return graph[n-1][m-1]

print(bfs(0, 0))