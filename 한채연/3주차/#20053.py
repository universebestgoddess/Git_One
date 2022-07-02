T = int(input())

# while T:
#     n = int(input())
#     nums = list(map(int, input().split()))
#     min, max = 1000001, -1000001
#     for i in nums:
#         if i < min:
#             min = i
#         if i > max:
#             max = i
#     print(min, max)
#     T -= 1

while T:
    n = int(input())
    nums = list(map(int, input().split()))
    print(min(nums), max(nums))
    T -= 1