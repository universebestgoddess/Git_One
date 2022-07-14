def sequential_search(n, target, array):
    for i in range(n):
        if target == array[i]:
            return i+1  # 현재 위치 반환
print("생성할 원소의 갯수를 입력하고 한 칸을 띄고 찾을 문자열을 입력해주세요.")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("입력한 숫자만큼 문자열을 입력하세요. (구분은 띄어쓰기로)")
array=input().split()

sequential_search(n, target, array)