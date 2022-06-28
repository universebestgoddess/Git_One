import sys

pos = sys.stdin.readline().rstrip()
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)]  # 8가지

cnt = 0
for i in moves:
    row = int(pos[1]) + i[1]
    column = int(ord(pos[0])) - 96 + i[0]
    if 1<= row <= 8 and 1 <= column <= 8:
        cnt += 1
print(cnt)