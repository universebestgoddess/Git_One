n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 12345
b.sort(reverse=True)  # 66555

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]   # 교체
    else:
        break

print(sum(a))
