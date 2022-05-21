# 내풀이
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
result = []
for i in range(N):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    nums.sort()
    result.append(nums[0])  # 각 행에서 최솟값을 넣어준다
result.sort(reverse=True)
print(result[0])  # 내림차순 정렬하고 가장 큰수 출력하기

# 답지풀이1
n, m = map(int, input().split())
result = 0

for i in range(n):
    nums = list(map(int, input().split()))
    min_num = min(nums)  # 가장 작은수 찾기
    result = max(result, min_num)  # 현재까지 숫자중 가장 큰수 찾기
print(result)

# 답지풀이2
n, m = map(int, input().split())
result = 0

for i in range(n):
    nums = list(map(int, input().split()))
    min_num = 10001
    for j in nums:
        min_num = min(min_num, j)  # 현재 행에서 가장 작은수 찾기
    result = max(result, min_num)

print(result)

