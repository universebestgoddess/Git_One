import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0

while True:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    else:  # 5로 나누어 떨어지지 않을때
        N -= 3
        if N < 0:
            print(-1)
            break
        cnt += 1