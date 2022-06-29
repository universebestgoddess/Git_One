N, K = map(int,input().split( ))

try_num = 0

while N>1:
    if N%K==0:
        N = N/K
        try_num +=1
    else:
        N -=1
        try_num +=1

print(try_num)