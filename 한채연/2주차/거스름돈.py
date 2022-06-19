n = 1260
count = 0
coins = [500, 100, 50, 10]  # 큰 단위부터 적어주기

for coin in coins:
    count += n // coin
    n = n % coin
print(count)