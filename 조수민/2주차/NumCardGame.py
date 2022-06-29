row, column = map(int, input().split())
minest = []

for i in range(row):
    data = map(int, input().split())
    min_data = min(data)
    minest.append(min_data)

result = max(minest)
print(result)
