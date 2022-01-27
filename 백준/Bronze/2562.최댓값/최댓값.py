nums = []

for i in range(9):
    n = int(input())
    nums.append(n)

print(max(nums), nums.index(max(nums))+1 )