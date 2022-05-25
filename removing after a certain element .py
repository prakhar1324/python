l = [int(x) for x in input(). split()]
x = int(input())
ls = []
for i in range(len(l)):
    if x!=l[i]:
        ls.append(l[i])
    else:
        break
print(ls)