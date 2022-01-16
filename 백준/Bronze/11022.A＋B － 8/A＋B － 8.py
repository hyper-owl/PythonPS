n = input()

n = int(n)

for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print("Case #{0}: {1} + {2} = {3}".format(i+1,a,b ,a+b))