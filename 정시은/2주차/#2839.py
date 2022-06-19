#배달할 설탕 nkg
n=int(input())
m=0 #봉지 개수
while n>=0:
    if n%5 == 0:
        m+=(n//5) #5로 나눈 몫이 봉지 개수가 됨
        print(m)
        break
    n-=3
    m+=1
else:
    print(-1)
