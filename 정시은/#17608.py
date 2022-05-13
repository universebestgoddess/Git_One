import sys
a= int(sys.stdin.readline())
stack=[]

for _ in range(a):
    bar= int(input())

    while stack and stack[-1] <= bar: #stack에 값이 있고 마지막값이 지금 입력받는 것보다 길이가 같거나 짧으면 pop
        stack.pop()
    stack.append(bar)

print(len(stack))


#시간초과
