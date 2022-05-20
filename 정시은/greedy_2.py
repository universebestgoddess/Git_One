#행과 열 분리해서 입력받기
n,m= map(int,input().split());

result = 0;
for i in range(n):
    data= list(map(int, input().split()))
    #행에서 가장 작은 수 찾기
    min_value= min(data)
    #가장 작은 수 중에서 가장 큰 수 찾기
    result= max(result, min_value); #max(min_value)

print(result)

