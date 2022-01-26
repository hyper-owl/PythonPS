ori = input()

ori = int(ori)

ans = 1

if ori < 10:
    ori = ori * 10

tar = ori

while True:
    one = tar % 10
    ten = tar // 10

    add = one + ten
    new = (one * 10) + (add % 10)

    if new == ori:
        break
    
    tar = new
    ans = ans + 1

print(ans)