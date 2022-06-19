# 거스름돈
N = int(input())
cnt = 0

exchange = [500, 100, 50, 10]

for i in exchange:
    cnt += N//i     # 잔돈 단위 순서대로 동전 개수를 센다.
    N = N % i          # i로 거슬러주고 남은 잔돈이 다시 for 루프로 돌아가게 한다.
print(cnt)
