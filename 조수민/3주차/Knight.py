coordinate = input()
x = int(coordinate[1])
y = int(ord(coordinate[0]))-int(ord('a'))+1  # 아스키코드 변환 ord ,ord('a')=97

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)]

try_num = 0

for t in steps:
    next_x = x + t[0]  
    next_y = y + t[1]
    
    if next_x <= 8 and next_x >= 1 and next_y <= 8 and next_y >= 1:
        try_num +=1

print(try_num)
