# 내 풀이
import sys
N, M, K = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort(reverse=True)  # 내림차순 정렬(큰수부터)
m1 = nums[0]  # 가장큰수
m2 = nums[1]  # 두번째로 큰수

cnt = M // (K+1)
sum = cnt * (m1*K + m2*1)

sum += (M-cnt*(K+1))*m1
print(sum)


# 답지풀이1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1  # 더할때마다 전체 횟수에서 1씩 빼주기
    if m == 0:
        break
    result += second
    m -= 1
print(result)


# 답지풀이2  *입력조건 체크하기
n, m, k = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()
first = data[n-1]
second = data[n-2]
count = (m//(k+1))*k  # 가장 큰수가 더해지는 횟수
count += m % (k+1)  # 나누어 떨어지지 않는 경우 고려

result = 0
result += count * first + (m-count)*second
print(result)