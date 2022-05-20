# [1, 2, 3, 4, 5] => 3, 1, 4, 3, 2 // 5번, 4번, 3번...
# 3 / 3+1=4 / 3+1+4=8 / 3+1+4+3=11 / 3+1+4+3+2=13
# 1 2 3 3 4 => [2, 5, 1, 4, 3] 인출시간을 오름차순 정렬해주고, 그 순서로

import sys
n = int(sys.stdin.readline().rstrip())
p_time = list(map(int, sys.stdin.readline().rstrip().split()))
p_time.sort()
cnt = 0

for i in range(len(p_time)):  # range(5)   5-4
    cnt += p_time[i] * (len(p_time) - i)
print(cnt)