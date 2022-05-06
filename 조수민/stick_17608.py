import sys
input = sys.stdin.readline

n = int(input())
sticks = [int(input()) for _ in range(n)]
max_height = sticks[-1]
cnt = 1

for i in range(n):
    if max_height < sticks[n-i-1]:
        cnt += 1
        max_height = sticks[n-i-1]
print(cnt)
