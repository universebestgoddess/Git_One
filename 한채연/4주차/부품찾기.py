import sys

n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in m_list:
    if i in n_list:
        print("yes", end=' ')
    else:
        print("no", end=' ')

# 이진탐색 알고리즘으로 풀기(다량의 데이터)
import sys
n = int(sys.stdin.readline().rstrip())
list1 = list(map(int, sys.stdin.readline().rstrip().split()))
list1.sort()  # 정렬

m = int(sys.stdin.readline().rstrip())
list2 = list(map(int, sys.stdin.readline().rstrip().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

for i in list2:
    result = binary_search(list1, i, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

# 계수정렬
n = int(sys.stdin.readline().rstrip())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().split()))

for i in x:
    if array[i] == 1:  # 부품이 존재
        print("yes", end=' ')
    else:
        print("no", end=' ')

# set() 함수 사용
n = int(sys.stdin.readline().rstrip())
array = set(map(int, sys.stdin.readline().rstrip().split()))
# print(array)  # {1, 3, 4, 6, 7}

m = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split()))

for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
