import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
height = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(height)

result = 0  #정답
while (start <= end):
    total = 0  # 합산한 떡의 양
    mid = (start+end) // 2
    for i in height:
        if i > mid:  # 떡의 길이 > 절단기 높이
            total += (i-mid)
    if total < m:  # 떡이 부족한 경우
        end = mid -1
    else:  # 떡이 충분한 경우
        result = mid
        start = mid + 1

print(result)