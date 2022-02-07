a = int(input())

for i in range(a):
    nums = [int(i) for i in input().split()]
    del nums[0]
    ave = sum(nums) / len(nums)
    ans = 0
    for i in nums:
        if i > ave:
            ans = ans + 1
    
    print("{:.3f}%".format(ans / len(nums) * 100))