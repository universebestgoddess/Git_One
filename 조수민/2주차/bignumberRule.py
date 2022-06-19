# 큰 수의 법칙
N, M, K = map(int, input().split())  # 배열의 크기:N, 숫자가 더해지는 횟수:M
# 연속으로 더할 수 있는 최대횟수:K

data = list(map(int, input().split()))  # 입력받은 리스트
# 최대 수들을 찾고 첫번째,2번째 수만 알고 번갈아 더하면 됨.

data.sort(reverse=True)
first = data[0]
second = data[1]
total = 0

while True:
    for i in range(K):
        if M == 0:
            break
        total += first
        M -= 1
    if M == 0:
        break
    total += second
    M -= 1

print(total)
