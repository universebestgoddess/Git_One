import sys

a= int(sys.stdin.readline())
stack=[]

for _ in range(a):
    sen= sys.stdin.readline().split() #입력받은걸 split
    orders= sen[0] #명령어 orders

    #명령어가 push라면
    if orders == "push":
        stack.append(sen[1])

    #size
    elif orders == "size":
        print(len(stack))

    #empty
    elif orders == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    #pop
    elif orders == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    #top
    elif orders == "top":
        if len(stack) ==0 : #stack.size() == 0 쓰면 안됨
            print(-1)
        else:
            print(stack[-1])
