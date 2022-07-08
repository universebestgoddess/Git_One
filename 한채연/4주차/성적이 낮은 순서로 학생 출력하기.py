n = int(input())
students=[]

for i in range(n):
    a = input().split()
    students.append((a[0], a[1]))

students.sort(key=lambda x: x[1])

for i in students:
    print(i[0], end=' ')