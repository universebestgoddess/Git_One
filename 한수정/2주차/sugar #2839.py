n=int(input()) #설탕양
result=0 #봉지

while n>=0:
    if n%5==0:
        result+=n//5 #5로 나눈 몫
        print(result)
        break #이 밑으로 더 진행하지 않는다.
    n-=3 #5의 배수가 될때까지 3키로 봉지에 담기
    result+=1 #궁금: 왜 여기선 결과 출력X?
else:
    print(-1)