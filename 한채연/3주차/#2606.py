comp = int(input())
n = int(input())
matrix = [[0]*(comp+1) for _ in range(comp+1)]  # 첫번째 인덱스는 비워둠
visited = [False] * (comp+1)  # 노드 방문 체크를 위한 리스트
# print(matrix)

for _ in range(n):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1  # 연결되어 있음을 표시
# print(matrix)
cnt = 0

# dfs
result=[]
def dfs(v):
    visited[v] = 1  # 방문처리
    for i in range(1, comp+1):
        if matrix[i][v] == 1 and visited[i] == 0:  # 연결되어 있고 아직 방문X
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))

# bfs
from collections import deque

def bfs(v):
    result=[]
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in range(1, comp+1):
            if matrix[i][v] == 1 and visited[i] == 0:
                visited[i] = 1  # 방문처리
                q.append(i)
                result.append(i)
    return len(result)

print(bfs(1))