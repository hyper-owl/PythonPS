a = int(input())
b = int(input())
c = int(input())

ans = list(map(int, str(a * b * c)))

for i in range(10):
    num = ans.count(i)
    print(num)