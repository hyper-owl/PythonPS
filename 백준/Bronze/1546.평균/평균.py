a = int(input())

nums = [int(i) for i in input().split()]

std = max(nums)

nums = [i/std for i in nums]
print(sum(nums) / len(nums) * 100)