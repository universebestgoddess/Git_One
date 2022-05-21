import sys
#첫째줄에는 사람의 수가 주어진다
n= int(input())
#둘째줄에는 각 사람이 돈을 인출하는데 걸리는 시간이 주어진다
time= list(map(int, sys.stdin.readline().split()))
time.sort()
min_time=0

for i in range(n):
    min_time += time[i]*(n-i)
print(min_time)