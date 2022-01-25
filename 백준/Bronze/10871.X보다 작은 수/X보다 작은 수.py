n, x = map(int, input().split())

nums = [int(i) for i in input().split()]

for i in nums:
    if i < x:
        print(i, end = ' ')