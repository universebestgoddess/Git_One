#n,m,k 를 공백으로 구분하여 입력받기
n,m,k= map(int,input().split());
#n개의 자연수
data=list(map(int,input().split()));

#data 정렬하기
data.sort();
first= data[n-1] #가장 큰 수
second= data[n-2] #두번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1))*k
count += m % (k+1)

result=0
result += (count)*first
result += (m-count) * second

print(result)