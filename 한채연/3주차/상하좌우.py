import sys

n = int(sys.stdin.readline().rstrip())
x, y = 1, 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
types = ['U', 'D', 'L', 'R']
plans = sys.stdin.readline().rstrip().split()

for plan in plans:
    for i in range(len(types)):
        if plan == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:  # 공간을 벗어나는 경우 이동X
        continue
    x, y = nx, ny

print(x, y)