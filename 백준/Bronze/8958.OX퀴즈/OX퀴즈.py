a = int(input())

for i in range(a):
    ans = list(str(input()))
    score = 0
    seq = 0
    for i in ans:
        
        if i == 'X':
            seq = 0
        else:
            seq = seq + 1
            score = score + seq
        
    print(score)