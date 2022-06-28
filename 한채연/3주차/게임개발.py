n, m = map(int, input().split())
x, y, direction = map(int, input().split())

matrix=[]  # 맵 입력받기
for _ in range(n):
    matrix.append(list(map(int, input().split())))

d = [[0]* m for _ in range(n)]  # 방문여부를 체크하기 위한 이차원 배열
d[x][y] = 1  # 방문처리

dx=[-1, 0, 1, 0]  # 북, 동, 남, 서 이동
dy=[0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1  # 왼쪽으로 90도 회전
    if direction == -1:  # 북쪽 바라볼 때 회전한 경우
        direction = 3

turn_time = 0
count = 1
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and matrix[nx][ny] == 0:  # 아직 방문 안한 경우 && 육지인 경우
        d[nx][ny] = 1  # 방문처리
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:  # 네방향 모두 이동 불가능한 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        if matrix[nx][ny] == 0:  # 뒤로 이동 가능한 경우(육지인 경우)
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)