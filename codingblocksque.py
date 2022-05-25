from re import I


n = int(input())
l = [int(x) for x in input().split()]
for i in l:
    k = 0
    unique = i
    for j in l:
        if i^j == 0:
            k += 1
            if k>1:
                break
        else:
            pass
    if k==1:
        break
print(unique)