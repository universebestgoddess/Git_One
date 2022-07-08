n = int(input())
nums=[]
for _ in range(n):
    nums.append(int(input()))
nums.sort(reverse=True)
# nums = sorted(nums, reverse=True)

for i in nums:
    print(i, end=' ')