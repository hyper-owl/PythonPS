num = []

for i in range(10):
    a = int(input())
    if num.count(a % 42) == 0:
        num.append(a % 42)

print(len(num))