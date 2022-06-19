import sys
a= int(sys.stdin.readline())

queue=[]

for _ in range(a):
    sen= sys.stdin.readline().split() #입력받은걸 split
    orders= sen[0] #명령어 orders

    if orders == "push":
        queue.append(sen[1])

    elif orders == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif orders == "size":
        print(len(queue))

    elif orders == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif orders == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0]) #큐의 가장 앞에 있는 정수를 출력한다

    elif orders == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1]) #큐의 가장 뒤에 있는 정수를 출력한다