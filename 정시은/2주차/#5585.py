#타로가 지불할 돈
value= int(input())
paidback= 1000- value
count=0
n= [500,100,50,10,5,1]
for i in n:
    count += paidback//i
    paidback %= i

print(count)