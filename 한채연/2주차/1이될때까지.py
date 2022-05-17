# 내 풀이
import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

while True:
    if N % K == 0:
        N = N // K  # 나눠주기
        cnt += 1
    else:
        N -= 1
        cnt += 1
    if N == 1:
        break
print(cnt)

# 답지풀이1 -> 가장 많이 나눠주는 것이 최적의 해를 보장
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:  # 나누어 떨어지지 않는 경우
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)

# 답지풀이2 -> 배수가 되도록 효율적으로 빼주기
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k  # 나누어 떨어지는 수인 target 찾기
    result += (n-target)  # 1씩 빼주는 횟수  더하고
    n = target  # n을 나누어 떨어지는 수인 target으로 업데이트
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)  # 나누어 떨어지지 않은 값에 해당하는 횟수 더해주기
print(result)