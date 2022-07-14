stud = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    stud.remove(a)

for i in stud:
    print(i)